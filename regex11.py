import re
a=raw_input("Enter a string")
if(re.search('is\s*\w*',a)):
	print("Found")
else:
	print("Not Found")

