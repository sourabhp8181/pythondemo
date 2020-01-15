import re
a=raw_input("Enter a string")
if(re.search('is\s*\w{2}',a)):
	print("Found")
else:
	print("Not Found")

