for j in range(1,1001):
	n=j
	sum=0
	for i in range(1,n):
		if n%i==0:
			sum=sum+i
		i=i+1
	if sum==n:
		print n,"is perfect"
