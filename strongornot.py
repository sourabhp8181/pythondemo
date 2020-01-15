def strong(n):
	sum=0
	while n>0:
		rem=n%10
		f=1
		for i in range(1,rem+1):
			f=f*i
		sum=sum+f
		n=n/10
	return sum
num=input('Enter a number')
s=strong(num)
if s==num:
	print num,"is strong number"
else:
	print num,"not a strong number"

