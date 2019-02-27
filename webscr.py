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
	print(result)
	data = result.find_all('td')
	gold_year.append(re.findall(r'[12]\d{3}', str(data)))
	#gold_price.append(re.findall(r'\$\d+(?:.(\d+))?', str(data)))

	#Error on gold prices. Check the regex

with open('goldpricehistoric2.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for x in range(len(gold_year)):
    	filewriter.writerow([gold_year[x]])#, gold_price[x]])

