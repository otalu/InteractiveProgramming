"""
Parses through the Wikipedia pages of countries and returns a dictionary of
their capitals.

Authors = Anupama Krishnan, Onur Talu
"""
from bs4 import BeautifulSoup
import urllib


dictOfURL = {}
webpage = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_sovereign_states')
soup = BeautifulSoup(webpage, 'lxml')
tableCountries = soup.find('table', {'class': 'sortable wikitable'})
entries = tableCountries.findAll('tr')
# print(entries)
for entry in entries:
    if entry.find('td', {'style': 'vertical-align:top'}):
        name_key = entry.find('a').getText().replace('\n', ' ')
        print(name_key)
        for anchor in soup.find_all('a'):
            url_value = anchor.get('href')
        dictOfURL[name_key] = url_value
print(dictOfURL)
