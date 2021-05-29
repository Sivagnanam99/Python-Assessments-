class Employee:
    __Ename="Siva"          # Private Data Members
    __Eno="12"
    __Edept="CS"
    __Esalary=12000
    def print_details(self):
        print("Employee Name:",self.__Ename)
        print("Employee Number:",self.__Eno)
        print("Employee Department:",self.__Edept)
        print("Employee Salary:",self.__Esalary)
     
def main():
    E=Employee()
    E.print_details()
        
if __name__ == "__main__":
    main()
