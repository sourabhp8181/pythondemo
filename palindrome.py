n=input('Enter a number')
sum=0
num=n
while n>0:
	rem=n%10
	sum=(sum*10)+rem
	n=n/10

if sum==num:
	print num,"is palindrome"
else:
	print num,"is not palindrome"