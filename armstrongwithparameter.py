def armstrong(n):
	sum=0
	num=n
	while n>0:
		rem=n%10
		sum=sum+(rem*rem*rem)
		n=n/10
	return sum

num=input('Enter a number')
s=armstrong(num)
if s==num:
	print num,"is an Armstrong no."
else:
	print num,"is not an Armstrong no."