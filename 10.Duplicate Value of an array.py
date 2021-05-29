
lst=[1,2,3,4,5,2,3,4,7,9,5]
lst1=[]
def duplicate_removal():
    for i in lst:
        if i not in lst1:
            lst1. append(i)
        else:
            print(i,end=' ')

duplicate_removal()
