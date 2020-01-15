f=open('abc.txt','r')
cnt=0
ch=f.read(1)
while len(ch) > 0:
	if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
		cnt=cnt+1
	ch=f.read(1)
print 'Number of vowels',cnt