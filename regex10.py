import re
a=raw_input("Enter a string")
if(re.search('good\s{1,4}boy',a)):
	print("Found")
else:
	print("Not Found")

