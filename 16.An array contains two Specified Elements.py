lst=[12,23,24,25]
def find_num():
    for i in lst:
        if(i==12 and i==23):
            print("Both 12 and 24 are Found")
            break
        elif(i==12 and i!=22):
            print("12 Only Found")
        elif(i!=12 and i==23):
            print("23 Found")
        else:
            print("Bye")
find_num()
