import re
a=raw_input("Enter a string")
if(re.search('is\s*\w*great',a)):
	print("Found")
else:
	print("Not Found")

