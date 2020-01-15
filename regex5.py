import re
a=raw_input("Enter a string")
if(re.search('best.*batsman',a)):
	print("Found")
else:
	print("Not Found")

