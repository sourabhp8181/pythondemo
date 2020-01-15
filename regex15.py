import re
a=raw_input("Enter a string")
if(re.search('[a-g][o-r][o-r]d\s*boy',a)):
	print("Found")
else:
	print("Not Found")

