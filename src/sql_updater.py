import mysql.connector
import config

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd=config.sql_pass,
	database="movies_db" 
) 

cursor = db.cursor(buffered=True)
cursor.execute('SET collation_connection = \"utf8_general_ci\";')

def addMovie(mID, original_title, opening_earnings, rotten_tomatoes, imdb_score, metacritic):
	cursor.execute('SELECT * FROM current_movies WHERE id = ' + str(mID))
	if (cursor.fetchone() != None):
		print ('Movie with id ' + str(mID) + ' already exists!')
	cursor.execute('INSERT INTO current_movies (id, title, opening_earnings, rotten_tomatoes, imdb_score, metacritic) VALUES (' + 
		str(mID) + ', \"' +
		original_title + '\", ' +
		str(opening_earnings) + ', ' +
		str(rotten_tomatoes) + ', ' +
		str(imdb_score) + ', ' +
		str(metacritic) +
		')')
	db.commit()

def clearMovies():
	cursor.execute('TRUNCATE best_movies')
	cursor.execute('DELETE FROM current_movies')

def commitMovies():
	db.commit()