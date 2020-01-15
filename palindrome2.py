for i in range(1,1001):
	n=i
	sum=0
	num=n
	while n>0:
		rem=n%10
		sum=(sum*10)+rem
		n=n/10

	if sum==num:
		print num,"is palindrome"
