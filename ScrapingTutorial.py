#import cs109style
#cs109style.customize_mpl()
#cs109style.customize_css()

import requests

from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/List_of_countries_by_past_and_future_population'
website_html = requests.get(url).text
website_html = BeautifulSoup(website_html)
#print(website_html.prettify())

table = website_html.find_all("table", class_="sortable wikitable")
#print(table)

for tbl in table:
	print(tbl('th')[1].contents)

def table_type(tbl):
	### Extract the table type
	return tbl('th')[1].contents

table_by_type = {}
for tbl in table:
	typ = table_type(tbl)
	if typ not in table_by_type:
		table_by_type[typ] = []  # equivalent to []
	table_by_type[typ].append(tbl)

## Equivalent code below

## group the tables by type
#tables_by_type = defaultdict(list)  
## defaultdicts have a default value that is inserted when a new key is accessed
#for tbl in table:
	#tables_by_type[table_type(tbl)].append(tbl)

#print(tables_by_type)


#def get_countries_population(table):
	#result = defaultdict(dict)
	
	#for tbl in tables:
		#headers = tbl('tr')
		#first_header = headers[0]
		#th_s = first_header('th')
		#years = [int(val.content) for val in th_s if val.content.isnumeric()]
		#year_indices = [idx for idx, val in enumerate(th_s) if val.content.isnumeric()]
		#print(years)
		#print(year_indices)
		#rows = tbl('tr')[1:]
		#for row in rows:
			#tds = row('td')
			#country_name = tds[1]('a')[0].content
			#population_by_year = [int(tds[colidx].content.replace(',', '')) for colidx in year_indices]
			#subdict = dict(zip(years, population_by_year))
			#result[country_name].update(subdict)
	#return result


#result = get_countries_population(tables_by_type[u'Country or territory'])
#print(len(result), "Countries extracted")
#print(result[u'Canada'])
