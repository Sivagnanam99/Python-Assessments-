class sample:
    a=int(input("Enter Employee Id"))  #Static Variables
    b=input("Enter Employee Name")
    print("Employee Id",a)
    print("Employee Name",b)
    def Emp(dep):      # instance variables
        return dep
    def Empl(self,salary):
        return salary

obj=sample()
obj.Emp=staticmethod(sample.Emp)
print("Emp Dept:",'cs')
obj.Empl=staticmethod(sample.Empl)
print("Emp Salary:",'1200')


    
