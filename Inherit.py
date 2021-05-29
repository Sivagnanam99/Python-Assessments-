class A:
    def printadd(self):
        print("Addition of Two Numbers.....")
    def add(self,a,b):
        print(a+b)
    def overridemethod(self):                   #Override Method
        print("Addition Completed")
        
class B(A):
    def printsub(self):
        print("Subration of two Numbers.....")
    def sub(self,a,b):
        print(a-b)
    def overridemethod(self):                   #Override Method
        print("Subraction Completed")
class C(B):
    def printmul(self):
        print("Multiplication of two numbers......")
    def mul(self,a,b):
        print(a*b)
    def overridemethod(self):                  #Override Method
        print("Multiplication Completed")

def main():
    print(" ************Inheritance In Python ***********")
    c=int(input("Enter First value"))
    d=int(input("Enter The Second value"))
    objA=A()
    objB=B()
    objC=C()
    objA.printadd()
    objA.add(c,d)
    objA.overridemethod()
    objB.printsub()
    objB.sub(c,d)
    objB.overridemethod()
    objC.printmul()
    objC.mul(c,d)
    objC.overridemethod()
if __name__ == "__main__":
    main()


