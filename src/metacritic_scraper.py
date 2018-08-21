from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from movie_utils import *
import sys
import re

def getPersonScore(person_name):
	adjustedName = (person_name.replace(' ', '-').replace('.', '')).lower()
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	search_url = 'http://www.metacritic.com/person/' + adjustedName
	headers= {'User-Agent':user_agent} 
	request=urllib.request.Request(search_url,None,headers) #The assembled request
	#response = urllib.request.urlopen(request)

	try:
	    response = urllib.request.urlopen(request)
	except urllib.error.HTTPError as e:
	    #if e.code == 404:
	    print ('Person not found!')
	    return -1

	search_html = response.read()
	search_soup = BeautifulSoup(search_html, "html.parser")
	td_list = search_soup.findAll('td', {'class':'summary_score'})
	print (td_list[0].get_text().replace('\n', ''))
	return int(td_list[0].get_text().replace('\n', ''))