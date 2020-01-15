import re
a=open('abc.txt','r')
x=a.read()
y=re.compile('boy')
y=y.sub('batsman','x')
print y
a=open('abc.txt','w')
x=a.write(y)
print "Task Completed"