class student:
	def __init__(self,a,b):
		self.id=a
		self.name=b

	def display(self):
		print(self.id,self.name)

ob=student(1,"Virat")
ob.display()