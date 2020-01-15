a=open('abc.txt','r')
s1=a.read()
i=len(s1)-1              #by Indexing
r=""
while i>=0:
	r=r+s1[i]
	i=i-1
c=open('pqr.txt','w')
s2=c.write(r)



