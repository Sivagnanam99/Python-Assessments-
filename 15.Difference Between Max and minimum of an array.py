lst=[1,2,3,4,5]
def max_min():
    print("Actual List",lst)
    max_number=max(lst)
    min_number=min(lst)
    diff=max_number-min_number
    print("Difference Of Maximum and Minimum of The array",diff)
max_min()
