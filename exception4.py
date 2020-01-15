try:
	a=input('Enter 1st number :')
	b=input('Enter 2nd number :')
	c=a/b
	print c
except:
	print'Exception occured please check input'
except(ZeroDivisionError):
	print'Denominator cannot be zero'

print'Exception Program'