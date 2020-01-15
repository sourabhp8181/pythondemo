'''must be right to left arrangement
Wrong pattern:(not allowed)
fun(a=0,b,c=0):
fun(a=0,b):'''


def fun(a=0,b=0,c=0):
	print a
	print b
	print c

fun()
fun(10)
fun(10,20)
fun(10,20,30)