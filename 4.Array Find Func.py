def search(list, inp):
    for i in range(len(list)):
        if list[i] == inp:
            return True
    return False


mylst = ['Surya', 'Siva', 'Hari', 'Venkat']
print(mylst)
inp=input("Enter The element To search")
if search(mylst,inp):
    print("found")
else:
    print("not found")
