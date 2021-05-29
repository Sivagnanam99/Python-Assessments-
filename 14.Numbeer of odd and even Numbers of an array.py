inp_lst=[]
odd_lst=[]
even_lst=[]
Lim=int(input("Enter the limit"))
for i in range(0,Lim):
    inp=int(input("Enter The elements"))
    inp_lst.append(inp)
print("Actual List",inp_lst)

for i in inp_lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print("List of Odd Numbers",odd_lst)
print("Number of Odd Numbers",len(odd_lst))
print("List of Even Numbers",even_lst)
print("Number of Even Numbers",len(even_lst))
    
