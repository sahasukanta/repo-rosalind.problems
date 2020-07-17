# DNA Reverse Complement

# accessing data
fileHandler = open(input("Enter File Name Here: "), 'r')
Data = fileHandler.read()

d2 = Data.replace('T', 't')
d3 = d2.replace('C', 'c')
d4 = d3.replace('A', 'T')
d5 = d4.replace('G', 'C')
d6 = d5.replace('t', 'A')
d7 = d6.replace('c', 'G')

# reversing DNA strand
dataReverse = d7[::-1]
print(dataReverse)









