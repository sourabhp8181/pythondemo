n=input('Enter a number')
num=n
sum=0

while n>0:
	rem=n%10
	sum=sum+(rem*rem*rem)
	n=n/10

if sum==num:
	print num,"is an Armstrong no."
else:
	print num,"is not an Armstrong no."