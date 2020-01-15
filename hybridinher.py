

class A:
	def fun1(self):
		print("In A")

class B(A):
	def fun2(self):
		print("In B")

class C:
	def fun3(self):
		print("In C")

class D(B,C):
	def fun4(self):
		print("In D")
ob=D()
ob.fun1()
ob.fun2()
ob.fun3()
ob.fun4()