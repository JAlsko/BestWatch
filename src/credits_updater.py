import mysql.connector
import requests
from metacritic_scraper import *
import config

api_key_tmdb = config.api_key_tmdb

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd=config.sql_pass,
	database="movies_db" 
) 

cursor = db.cursor()
cursor.execute('SET collation_connection = \"utf8_general_ci\";')

def updateCredits(movie_id):
	cursor.execute('SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = \"movie_' + str(movie_id) + '\" AND TABLE_SCHEMA = \"credits\";')
	if (cursor.fetchone() != None):
		#cursor.execute('DROP TABLE credits.movie_' + str(movie_id) + ';')
		print ('Movie with ID ' + str(movie_id) + ' already has cast credits table')
		return
	mCredReq_tmdb = requests.get('https://api.themoviedb.org/3/movie/' + str(movie_id) + '/credits?api_key=' + api_key_tmdb)
	mCredRes_tmdb = mCredReq_tmdb.json()
	#print (mCredRes_tmdb)
	table_name = "credits.movie_" + str(movie_id)

	cursor.execute("CREATE TABLE " + table_name + " (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, person_id INTEGER, role TEXT, character_name TEXT, acting_order INTEGER DEFAULT 0, FOREIGN KEY (person_id) REFERENCES movies_db.movie_people (person_id));")

	insert_command = 'INSERT INTO ' + table_name + ' (person_id, role, character_name, acting_order) VALUES '
	person_id = 0
	role = ""
	character_name = ""
	acting_order = 0
	for actor in mCredRes_tmdb['cast']:
		cursor.execute('SELECT person_id FROM movie_people WHERE name = \"' + actor['name'] + '\";')
		metacritic_score = getPersonScore(actor['name'])
		if (cursor.fetchone() == None):
			if actor['profile_path'] == None:
				cursor.execute('INSERT INTO movie_people (name, gender, profile_path, metacritic_score) VALUES (\"' + actor['name'] + '\", ' + str(actor['gender']) + ', NULL, ' + str(metacritic_score) + ');')
			else:
				cursor.execute('INSERT INTO movie_people (name, gender, profile_path, metacritic_score) VALUES (\"' + actor['name'] + '\", ' + str(actor['gender']) + ', \"' + actor['profile_path'] + '\", ' + str(metacritic_score) + ');')
			db.commit()
		else:
			cursor.execute('UPDATE movie_people SET metacritic_score = ' + str(metacritic_score) + ' WHERE name = \"' + actor['name'] + '\";')
			db.commit()
		cursor.execute('SELECT person_id FROM movie_people WHERE name = \"' + actor['name'] + '\";');
		
		person_id = cursor.fetchone()[0]
		role = "actor"
		character_name = actor['character'].replace('\'', '')
		acting_order = actor['order']

		insert_command += '(' + str(person_id) + ', \'' + role + '\', \'' + character_name + '\', ' + str(acting_order) + '), '
	insert_command = insert_command[:-2]
	insert_command += ';'
	cursor.execute(insert_command)
	db.commit()

#updateCredits(345940)