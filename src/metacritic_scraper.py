from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from movie_utils import *
import sys
import re

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent':user_agent} 

def getPersonScore(person_name):
	adjustedName = (person_name.replace(' ', '-').replace('.', '')).lower().encode('ascii', 'ignore').decode('ascii')
	search_url = 'http://www.metacritic.com/person/' + adjustedName
	request = urllib.request.Request(search_url,None,headers) #The assembled request
	#response = urllib.request.urlopen(request)

	try:
	    response = urllib.request.urlopen(request)
	except urllib.error.HTTPError as e:
	    #if e.code == 404:
	    print (person_name + ' not found!')
	    return -1

	search_html = response.read()
	search_soup = BeautifulSoup(search_html, "html.parser")
	td_list = search_soup.findAll('td', {'class':'summary_score'})
	if (len(td_list) <= 0):
		print (person_name + ' not found!')
		return -1
	#print (td_list[0].get_text().replace('\n', ''))
	return safe_cast(td_list[0].get_text().replace('\n', ''), int, default=0)