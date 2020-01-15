class student:
	def initialize(self,a,b):
		self.id=a
		self.name=b

	def display(self):
		print(self.id,self.name)

ob=student()
x=int(input("Enter rollno."))
y=input("Enter name")
ob.initialize(x,y)
ob.display()
