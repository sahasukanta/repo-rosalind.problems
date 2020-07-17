# RNA to Protein conversion

# for converting list to string
def listToString(lis):
    str1 = ""
    # traverse in the string
    for c in lis:
        str1 = str1 + c
    return str1

# for reading string formatted genome into codons and matching with the corresponding protein
def codonToProtein(seq):
    # for converting large genome into codon entries into list format
    codon_list = [(seq[i:i+3]) for i in range(0, len(seq), 3)]
    # for reading codons into corresponding protein and creating a new list with protein letters
    protein_list = []
    for c in codon_list:
        if c == 'UUU' or c == 'UUC':
            protein_list.append('F')

        elif c == 'UUA' or c == 'UUG' or c == 'CUU' or c == 'CUC' or c == 'CUA' or c == 'CUG':
            protein_list.append('L')

        elif c == 'UCU' or c == 'UCC' or c == 'UCA' or c == 'UCG' or c == 'AGU' or c == 'AGC':
            protein_list.append('S')

        elif c == 'UAU' or c == 'UAC':
            protein_list.append('Y')

        elif c == 'UGU' or c == 'UGC':
            protein_list.append('C')

        elif c == 'UGG':
            protein_list.append('W')

        elif c == 'CCU' or c == 'CCC' or c == 'CCA' or c == 'CCG':
            protein_list.append('P')

        elif c == 'CAU' or c == 'CAC':
            protein_list.append('H')

        elif c == 'CAA' or c == 'CAG':
            protein_list.append('Q')

        elif c == 'AGA' or c == 'AGG' or c == 'CGU' or c == 'CGC' or c == 'CGA' or c == 'CGG':
            protein_list.append('R')

        elif c == 'AUU' or c == 'AUC' or c == 'AUA':
            protein_list.append('I')

        elif c == 'AUG':
            protein_list.append('M')

        elif c == 'ACU' or c == 'ACC' or c == 'ACA' or c == 'ACG':
            protein_list.append('T')

        elif c == 'AAU' or c == 'AAC':
            protein_list.append('N')

        elif c == 'AAA' or c == 'AAG':
            protein_list.append('K')

        elif c == 'GUU' or c == 'GUC' or c == 'GUA' or c == 'GUG':
            protein_list.append('V')

        elif c == 'GCU' or c == 'GCC' or c == 'GCA' or c == 'GCG':
            protein_list.append('A')

        elif c == 'GAU' or c == 'GAC':
            protein_list.append('D')

        elif c == 'GAA' or c == 'GAG':
            protein_list.append('E')

        elif c == 'GGU' or c == 'GGC' or c == 'GGA' or c == 'GGG':
            protein_list.append('G')
    # using created func. to convert protien list into string format
    final_answer = listToString(protein_list)
    return final_answer

# for accessing files
fHandle = open(input('Enter File Name Here: ', 'r')
data_in_list_format = fHandle.readlines()
data_in_string = listToString(data_in_list_format)

# final answer
print(codonToProtein(data_in_string))












