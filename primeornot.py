n=input('Enter a number')
flag=0
i=2
while i<n:
	if n%i==0:
		flag=1
		break
	i=i+1
if flag==1:
	print n,"is composite"
else:
    print n,"is prime" 
