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
def add_to_csv(gold_year, gold_price, filename):
	
    with open(filename, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
    	for x in range(len(gold_year)):
    		filewriter.writerow([gold_year[x], gold_price[x]])

# This function only cleans YEAR data, one per row. 
def cleansing_year_data(gold_year):

	for value in gold_year:
		if len(value) > 1: # There's more than one year in the same position
			i = 0
			for data in value:
				#print(data)
				year_list.append(data)
				i =+ 1

		if len(value) == 1: # There's only one year in the given position
			year_list.append(value)

	print("Found yearly data: " +str(len(year_list)))

# Since currency has a different data treatment, a different function can detect the currency values needed.
def capture_currency(data):
	currency_found = True
	mule = data
	#i = 0
	#print(mule)

	while currency_found:
		match = re.search(r'\$\d+(?:.(\d+))*', str(mule))
		
		if match is not None:
			gold_price.append(match.group())
			mule = mule.replace(match.group(), ' ', 1)
			#i+=1

		if match is None:
			#print("Currency found within the data: " + str(i))
			currency_found = False


url = "http://onlygold.com/Info/Historical-Gold-Prices.asp"

page = urlopen(url)
soupHelper = BeautifulSoup(page, 'html.parser')

priceTable = soupHelper.find('table', attrs={'class' : 'TutorialMainTextFont fancy'})
prices = priceTable.find_all('tr')

gold_year = []
gold_price = []
year_list = []

for result in prices:
	#print(result)
	data = result.find_all('td')
	gold_year.append(re.findall(r'[12]\d{3}', str(data)))
	capture_currency(str(data))
	#gold_price.append(re.findall(r'\$\d+(?:.(\d+))?', str(data)))
	#Error on gold prices. findall works differently. Check how it works within this function
print("Found currency data: " + str(len(gold_price)))
cleansing_year_data(gold_year)
add_to_csv(year_list, gold_price, 'gold_value_since_1792.csv')

