class Sample:
    def add(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0
def main():
    a=int(input("Enter First Number"))
    b=float(input("Enter second Number"))
    obj = Sample()
# zero argument
    print("No argument:", obj.add())
# one argument
    print("SquareValue:", obj.add(a))
# two argument
    print("Multiplication Value:", obj.add(a,b))

main()
