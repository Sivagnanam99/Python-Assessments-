try:
    a=10/0
    print(a)
except (ArithmeticError,ValueError,FileNotFoundError):
    print("Can't Divisible by 0")
    
