class Compute:
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0
def main():
    a=int(input("Enter First Number"))
    b=int(input("Enter second Number"))
    obj = Compute()
# zero argument
    print("Area Value:", obj.area())
# one argument
    print("Area Value:", obj.area(a))
# two argument
    print("Area Value:", obj.area(a,b))

main()
