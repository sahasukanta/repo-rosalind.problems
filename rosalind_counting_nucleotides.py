# Counting Nucleotides

# accessing data
fileHand = open('rosalind_dna (2).txt')
readFile = fileHand.read()

# counting
A = readFile.count('A')
T = readFile.count('T')
C = readFile.count('C')
G = readFile.count('G')

# final answer
print(A, C, G, T)






