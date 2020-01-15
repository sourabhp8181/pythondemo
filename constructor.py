#Constructor:A special member fuction which gets automatically called when the object is created.

class student:
	def __init__(self):
		self.id=1
		self.name="Virat"

	def display(self):
		print(self.id,self.name)

ob=student()
ob.display()