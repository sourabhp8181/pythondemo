import re
a=raw_input("Enter a string")
if(re.search('bestbatsman',a)):
	print("Found")
else:
	print("Not Found")