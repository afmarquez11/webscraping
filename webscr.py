#Libraries
from bs4 import BeautifulSoup
import csv
import time
import re
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# Historic Gold prices example

# This function adds the values to a csv file.
def add_to_csv(gold_year, gold_price):
	
    with open('goldpricehistoric2.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
    	for x in range(len(gold_year)):
    		filewriter.writerow([gold_year[x], gold_price[x]])

# This function only cleans YEAR data, one per row. 
def cleansing_year_data(gold_year):

	year_list = []

	for value in gold_year:
		if len(value) > 1: # There's more than one year in the same position
			i = 0
			for data in value:
			#	print(data)
				year_list.append(data[i])
				i =+ 1

		if len(value) == 1: # There's only one year in the given position
			year_list.append(value)
	print(len(year_list))

url = "http://onlygold.com/Info/Historical-Gold-Prices.asp"

page = urlopen(url)
soupHelper = BeautifulSoup(page, 'html.parser')

priceTable = soupHelper.find('table', attrs={'class' : 'TutorialMainTextFont fancy'})
prices = priceTable.find_all('tr')

gold_year = []
gold_price = []

for result in prices:
	#print(result)
	data = result.find_all('td')
	gold_year.append(re.findall(r'[12]\d{3}', str(data)))
	#gold_price.append(re.findall(r'\$\d+(?:.(\d+))?', str(data)))
	#Error on gold prices. findall works differently. Check how it works within this function

cleansing_year_data(gold_year)

