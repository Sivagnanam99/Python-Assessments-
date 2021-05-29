def getMissingNo(A):
	n = len(A)
	total = (n + 1)*(n + 2)/2
	sum_of_A = sum(A)
	return total - sum_of_A


A = []
for i in range(2,100):
    A.append(i)
miss = getMissingNo(A)
print(miss)
