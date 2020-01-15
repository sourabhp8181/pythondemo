import re
a=raw_input("Enter a string")
if(re.search('[a-g]ood\s* is *boy',a)):
	print("Found")
else:
	print("Not Found")

