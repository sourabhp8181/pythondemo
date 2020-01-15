a=open('abc.txt','r')
s=a.read()
r=""
r=s[::-1]
b=open('pqr.txt','w')
b.write(r)

a.close()
b.close()
