a=open('abc.txt','r')
s1=a.read()
b=open('pqr.txt','r')
s2=b.read()
a=open('abc.txt','w')
b=open('pqr.txt','w')
a.write(s2)
b.write(s1)

