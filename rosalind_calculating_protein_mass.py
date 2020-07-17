# calculating protein mass

# mass dictionary
amino_acid_mass = {'A' : 71.03711, 'C' : 103.00919, 'D' : 115.02694, 'E' : 129.04259, 'F' : 147.06841, 'G' : 57.02146, 'H' : 137.05891, 'I' : 113.08406, 'K' : 128.09496, 'L' : 113.08406,
'M' : 131.04049, 'N' : 114.04293, 'P' : 97.05276, 'Q' : 128.05858, 'R' : 156.10111, 'S' : 87.03203, 'T' : 101.04768, 'V' : 99.06841, 'W' : 186.07931, 'Y' : 163.06333 }

# accessing data
fHandle = open(input("Enter File Name Here: "))
read_data = fHandle.read()

def listToString(data):
    empty_str = ""
    for line in data:
        empty_str = empty_str + line
    empty_str1 = empty_str.replace('\n',"")
    return empty_str1

# print(listToString(read_data))

# to access each value in the dict
# print(amino_acid_mass["A"])
# to sum up a list of integers
list1 = [1, 3, 4, 5]
# print(sum(list1))

def sum_protein_mass(seq):
    data_string = listToString(seq)
    template_var = "empty"
    listed_mass = []
    for c in data_string:
        template_var = c
        listed_mass.append(amino_acid_mass[template_var])
    total = sum(listed_mass)
    return total

print(sum_protein_mass(read_data))




