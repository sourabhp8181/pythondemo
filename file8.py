f1=open('abc.txt','r')

f2=open('pqr.txt','r')

s1=""
ch1=f1.read(1)
while len(ch1)>0:
	s1=s1+ch1
	ch1=f1.read(1)

s2=""
ch2=f2.read(1)
while len(ch2)>0:
	s2=s2+ch2
	ch2=f2.read(1)

s3=s1+s2
f3=open('xyz.txt','w')
f3.write(s3)