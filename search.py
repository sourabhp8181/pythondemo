import re
x='virat is good boy'
if(re.search('Good',x,re.I)): #I:Ignore case
	print "Found"
else:
	print "Not Found"