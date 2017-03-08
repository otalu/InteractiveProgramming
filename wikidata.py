"""
Parses through the Wikipedia pages of countries and returns a dictionary of
their capitals.

Authors = Anupama Krishnan, Onur Talu, Evan New-Schmidt
"""

from bs4 import BeautifulSoup
import urllib


def get_dictionary(country):
    webpage = urllib.request.urlopen('https://en.wikipedia.org/wiki/%s' % country)
    soup = BeautifulSoup(webpage, 'lxml')
    pageinfobox = soup.find('table', {'class': 'infobox'})
    entries = pageinfobox.findAll('tr')
    dictOfEntries = {}
    for entry in entries:
        if entry.find('th', {'scope': 'row'}):
            question_key = entry.find('th', {'scope': 'row'}).getText().replace('\n', ' ')
            answer_value = entry.find('td').getText()
            dictOfEntries[question_key] = answer_value
            return dictOfEntries


def get_capital(country):
    dictOfEntries = get_dictionary(country)
    if 'Capital' in dictOfEntries:
        print(dictOfEntries['Largest City'])
    if 'Capital and largest city' in dictOfEntries:
        print(dictOfEntries['Capital and largest city'])
    else:
        print(dictOfEntries)


if __name__ == "__main__":
    country = 'Iceland'
    get_capital(country)
