class samp:
    def __init__(self):
        self.a=7
    def print1(self):
        print(self.a)
class samp1:
    def __init__(self,b,c):
        self.b=b
        self.c=c
    def print2(self):
        print(self.b)
        print(self.c)
class samp2:
    def __init__(self,d,e,f):
        self.d=d
        self.e=e
        self.f=f
    def print3(self):
        print(self.d)
        print(self.f)
        print(self.e)
def main():
    ob=samp()
    ob.print1()
    ob1=samp1("12","2")
    ob1.print2()
    ob2=samp2(22,23,24)
    ob2.print3()
main()
        
