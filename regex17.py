import re
a='Virat isis is is good boy'
x=re.findall('is\s*is',a)
print len(x)