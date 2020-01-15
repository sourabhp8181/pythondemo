def demo():
		try:
			a=input('Enter 1st number :')
			b=input('Enter 2nd number :')
			c=a/b
			print c
			return
		except:
			print'Exception occured'
		finally:

			print'Exception Program'
demo()