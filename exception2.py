try:
	a=input('Enter 1st number :')
	b=input('Enter 2nd number :')
	c=a/b
	print c
	print 'Exception Program'
except(ZeroDivisionError):
	print'Denominator Cannot Be Zero'
except(NameError):
	print'Only integers allowed !!!'

	print'Exception Program'