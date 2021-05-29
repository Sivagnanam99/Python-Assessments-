def increment(a):
    return a+1
def decrement(b):
    return a-1
s=int(input("Enter the number"))
print("1.Increment \n 2.Decrement")
ch=int(input("Enter your Choice"))
if(ch==1):
    print(increment(s))
else:
    print(decrement(s))
