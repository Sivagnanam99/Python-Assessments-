s = "I am Global Variable"
def f():
	s = "I am Local variable s"
	print(s)

f()
print(s)
