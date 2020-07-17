# Highest GC Content

# defining func. to read .txt file and return data from each line in list format
def readFile(filePath):
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

# assigning variables and accessing data file
FASTAFile = readFile(input("Enter File Name Here: "))       # file handle
FASTADict = {}                                              # creating empty dict for later use while assigning key (>Rosalind_xxx) to values (genome)
FASTALabel = ""                                             # creating empty list for holding values (genome)

# for loop to loop through each line and assign each key to its values into the empty dict.
for lin in FASTAFile:
    if '>' in lin:
        # if line starts with '>', assign it as a new key, and then assign the next lines into the dict under this key.
        FASTALabel = lin
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += lin

# defining func. to calculate GC content
def gc_content(seq):
    return round((100*((seq.count('G') + seq.count('C'))/len(seq))), 6)

# calling all the given genomes and their GC content
ResultDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

# calling the max value
MaxGCKey = max(ResultDict, key=ResultDict.get)

# final answer
print(f'{MaxGCKey[1:]}\n{ResultDict[MaxGCKey]}')
