from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import re

def getOpeningEarnings(movie_title):
	adjustedTitle = re.sub(r'[^\w\s]','',movie_title).replace(' ', '%20').lower()
	search_url = 'https://www.boxofficemojo.com/search/?q=' + adjustedTitle + '&sort=date&sortrev=1&showpage=1&p=.htm'
	search_html = urlopen(search_url).read()
	search_soup = BeautifulSoup(search_html, "html.parser")
	td_list = search_soup.findAll('td')
	if len(td_list) < 16:
		print ("Movie not found!")
		return ("N/A")
	else:
		amount = search_soup.findAll('td')[15].get_text()
		print (amount)
		return amount.replace('$', '')

getOpeningEarnings(sys.argv[1])