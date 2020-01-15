import re
a=raw_input("Enter a string")
if(re.search('[1-4][5-9]',a)):
	print("Found")
else:
	print("Not Found")

