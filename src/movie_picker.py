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

def getCriticsPick():
	cursor.execute('SELECT * FROM current_movies ORDER BY metacritic + rotten_tomatoes DESC')
	topResult = cursor.fetchone()
	if (topResult == None):
		print ('Current movies list empty!')
		return
	return topResult[0]

def getAudienceFavorite():
	cursor.execute('SELECT *, (opening_earnings/10000000)+imdb_score AS audience_score FROM current_movies ORDER BY audience_score DESC;')
	topResult = cursor.fetchone()
	if (topResult == None):
		print ('Current movies list empty!')
		return
	return topResult[0]

def getBestCast():
	return

def clearPicks():
	cursor.execute('DELETE FROM best_movies WHERE id = 1 OR id = 2 OR id = 3')

def updateBestMovies():
	criticsPick = getCriticsPick()
	audienceFavorite = getAudienceFavorite()
	clearPicks()

	cursor.execute('INSERT INTO best_movies (id, m_id) VALUES (1, ' + str(criticsPick) + '), (2, ' + str(audienceFavorite) + ')')
	db.commit()

def commitMovies():
	db.commit()