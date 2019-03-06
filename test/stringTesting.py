import re
gold_year = []
prueba = True
text ='[<td><div align="center">1912</div></td>, <td><div align="right">$20.67</div></td>, <td bgcolor="#F0E8DD" rowspan="15"></td>, <td><div align="center">1897</div></td>, <td> $20.67</td>, <td bgcolor="#F0E8DD" rowspan="15"></td>, <td><div align="center">1882</div></td>, <td width="75"><div align="right">$20.67</div></td>, <td bgcolor="#F0E8DD" rowspan="15">\xa0</td>]'

currency_found = True
mule = text
while currency_found:
	match = re.search(r'\$\d+(?:.(\d+))*', str(mule))
	
	if match is not None:
		gold_year.append(match.group())
		print(match.group())
		mule = mule.replace(match.group(), ' ')
	

	if match is None:
		currency_found = False


