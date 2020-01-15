f=open('abc.txt','r')
Lcnt=0
tcnt=0
scnt=0
ccnt=0
ch=f.read(1)
while len(ch)>0:
	if(ch=='\n'):
		Lcnt=Lcnt+1
	if(ch==' '):
		scnt=scnt+1
	if(ch=='\t'):
		tcnt=tcnt+1
	ccnt=ccnt+1
	ch=f.read(1)

print "No. of lines",Lcnt
print "No. of spaces",scnt
print "No. of tabs",tcnt
print "No. of characters",ccnt


