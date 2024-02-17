from math import pow

def make_pow(n):
	def inner_func(x):
		return pow(x,n)
	return inner_func

test1 = make_pow(4)
print(test1) 
a = test1(5)
print(a)
