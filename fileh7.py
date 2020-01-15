a=open('abc.txt','r')
s1=a.read()
b=open('pqr.txt','r')
s2=b.read()
c=open('xyz.txt','w')
s3=s1+s2
c.write(s3)

