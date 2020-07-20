# Finding motif
import re

# accessing data
fHandle = open(input("Enter File Name Here: "))
read = fHandle.readlines()
strA_0 = "".join(read[:-1])
strA_1 = strA_0.replace('\n', '')
strB_0 = read[-1]
strA = strA_1             # DNA to work with
strB = strB_0             # DNA pattern to be looked for

# creating list of all starting positions where pattern matches with str (including overlapping matches)
list1 = [match.start() for match in re.finditer('(?={})'.format(strB), strA)]
# fixing the index for starting with 0
list2 = [item+1 for item in list1]

# final output
print(list2)


