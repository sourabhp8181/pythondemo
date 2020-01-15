#Inheritance:Ability of one class to acquire properties of another class.

#Single Inheritance
class A:
	def fun1(self):
		print("In A")    #Single Inheritance

class B(A):
	def fun2(self):
		print("In B")

ob=B()
ob.fun1()
ob.fun2()