import requests
from sql_updater import *
from box_office_scraper import *
from movie_utils import *
from credits_updater import *
import config

api_key_tmdb = config.api_key_tmdb
api_key_imdb = config.api_key_imdb

def getPlayingMovies(language='en'):
	nowPlayingReq_tmdb = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=' + api_key_tmdb + '&language=en-US&page=1')
	nowPlayingRes_tmdb = nowPlayingReq_tmdb.json()['results']
	moviesList = []
	for m in nowPlayingRes_tmdb[:]:
		mID = m['id']
		mReq_tmdb = requests.get('https://api.themoviedb.org/3/movie/' + str(mID) + '?api_key=' + api_key_tmdb + '&language=en-US')
		mRes_tmdb = mReq_tmdb.json()
		updateCredits(mID)
		if mRes_tmdb['original_language'] != language:
			continue
		moviesList.append(m)

def main():
	nowPlayingReq_tmdb = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=' + api_key_tmdb + '&language=en-US&page=1')
	nowPlayingRes_tmdb = nowPlayingReq_tmdb.json()['results']
	clearMovies()
	for m in nowPlayingRes_tmdb[:]:
		mID = m['id']

		mReq_tmdb = requests.get('https://api.themoviedb.org/3/movie/' + str(mID) + '?api_key=' + api_key_tmdb + '&language=en-US')
		mRes_tmdb = mReq_tmdb.json()

		if mRes_tmdb['original_language'] != 'en':
			continue

		#print ('\n' + mRes_tmdb["original_title"] + '\n')
		#print (mRes_tmdb)


		imdbID = mRes_tmdb['imdb_id']
		original_title = mRes_tmdb["original_title"]
		mReq_imdb = requests.get('http://www.omdbapi.com/?i=' + imdbID + '&apikey=' + api_key_imdb)
		mRes_imdb = mReq_imdb.json()
		ratings = mRes_imdb['Ratings']
		#print ('\n' + original_title + ': ', end='')
		rotten_tomatoes = 0
		imdb_score = 0
		metacritic = 0
		for r in ratings:
			src = r['Source']
			val = r['Value']
			if src == 'Rotten Tomatoes':
				rotten_tomatoes = safe_cast(val.replace('%',''), int, default=0)
			elif src == 'Internet Movie Database':
				imdb_score = safe_cast((val[:val.index('/')]).replace('.',''), int, default=0)
			elif src == 'Metacritic':
				metacritic = safe_cast(val[:val.index('/')], int, default=0)
			#print(r['Source'] + ': ' + r['Value'] + ', ', end='')

		opening_earnings = getOpeningEarnings(original_title)

		addMovie(mID, original_title, opening_earnings, rotten_tomatoes, imdb_score, metacritic)

	#print('\n')
	getMovies(5)
	commitMovies()
	closeCursor()

getPlayingMovies()