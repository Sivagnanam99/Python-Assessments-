class siva:
    def add(self,a,b):
        return a+b
    def add(self,c,d):
        return c+d
def main():
    ob=siva()
    res1=ob.add(12,2)
    res2=ob.add(25,25)
    print("Addition Result of First Pair",res1)
    print("Addition Result of Second Pair",res2)
main()
