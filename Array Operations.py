lst1=["Surya","Siva","Hari","Praba","Sankar","Hema","Latha","Lalitha","Vidhya","Suba"]
print("Actual List:",lst1)
print("\n")
print("1.Add An Element Udhaya into the List1",lst1.append("Udhaya"))
print("After Adding",lst1)
print("\n")
print("2.Iterate Array Elements:")
for i in lst1:
    print(i)
print("\n")
print("3.Add an element with the specific Index 3",lst1.insert(3,"Chithra"))
print("After Adding",lst1)
print("\n")
print("3.Remove an Element (Surya) From  the list")
lst1.remove("Surya")
print("After removing Surya",lst1)
print("\n")
print("4.Update the element")
lst1.insert(1,"Priya")
print("After Updating",lst1)
print("\n")
print("5.Check if Name pavithra is present the list or not")
if(lst1=="Pavithra"):
    print("Pavithra Present")
else:
    print("Pavithra Not Present")
print("\n")
print("6.Size Of the List:",len(lst1))
print("\n")
print("7.Insert an element into the particular index:")
lst1.insert(7,"Uma")
print("After Inserting Uma",lst1)
print("\n")
print("8.Remove All Elements of List")
print("After Reoving All Elements of List",lst1.clear())
print(lst1)