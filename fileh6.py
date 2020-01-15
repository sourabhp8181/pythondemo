a=open('abc.txt','r')
ch=a.read()
x=raw_input('Enter a string')

if x in ch :
	print 'Found'
else:
	print 'Not Found'
