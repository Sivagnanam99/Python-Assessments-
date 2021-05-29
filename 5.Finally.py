try:
    a=10/0
    print(a)
except ArithmeticError:
    print("Arithmetic Error Exception Occurs")
finally:
    print("I am Always Executing")
