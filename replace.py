import re
x=raw_input('\n Enter a string \n')
y=re.compile('boy')
y=y.sub('batsman',x)
print y