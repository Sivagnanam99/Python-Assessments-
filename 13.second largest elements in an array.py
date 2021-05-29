a=[]
n=int(input("Enter number of elements:"))
def second_largest_element():
    for i in range(1,n+1):
        b=int(input("Enter element:"))
        a.append(b)
    a.sort()
    print("Second largest element is:",a[n-2])
second_largest_element()
