# DNA to RNA

# accessing data
fileHandler = open('rosalind_rna (3).txt','r')
Data = fileHandler.read()

# final answer
print(Data.replace('T', 'U'))
