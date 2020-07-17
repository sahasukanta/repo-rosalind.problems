# enumerating gene orders

from itertools import permutations

# accessing data
fHandle = open(input("Enter File Name Here: "))
data = fHandle.read()

# data number correction for range()
data1 = int(data) + 1

# permutation combination func. from itertools
a = list(permutations(range(1, data1)))
print(len(a))
for item in a:
    item = str(item)
    item = item.replace("(", "")
    item = item.replace(")", "")
    item = item.replace(",", "")
    print(item)


