#Libraries
from bs4 import BeautifulSoup
import csv
import time
import re
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

#Historic Gold prices example

url = "http://onlygold.com/Info/Historical-Gold-Prices.asp"

page = urlopen(url)
soupHelper = BeautifulSoup(page, 'html.parser')

priceTable = soupHelper.find('table', attrs={'class' : 'TutorialMainTextFont fancy'})
prices = priceTable.find_all('tr')

gold_year = []
gold_price = []

for result in prices:
	data = result.find_all('td')
	year = re.search(r'[12]\d{3}', str(data))
	value = re.search(r'\$\d+(?:.(\d+))?', str(data))
	if year is not None: #Found a year
		gold_year.append(year.group())
	if value is not None: #Found a value
		gold_price.append(value.group())

with open('goldpricehistoric.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for x in range(len(gold_year)):
    	filewriter.writerow([gold_year[x], gold_price[x]])

print("Hello")		