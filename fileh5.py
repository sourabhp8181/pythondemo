f1=open('abc.txt','r')
f2=open('pqr.txt','w')
ch=f1.read(1)
while len(ch)>0:
	f2.write(ch)
	ch=f1.read(1)
f1.close()
f2.close()