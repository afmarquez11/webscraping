import re
gold_year = []
prueba = True
text = '<td bgcolor="#FFF8E8" align="right">$383.25 $456.32</td>'


gold_year = re.findall(r'\$\d+(?:.(\d+))?', text)

for x in gold_year:
	print(x)