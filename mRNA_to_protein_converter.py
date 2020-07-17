# DNA/mRNA to Amino Acid Sequence Converter

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
    # list 1 to return as a str for direct output
    # list 2 to return for further operations to create amino acid counter dict.
    protein_list1 = []
    protein_list2 = []

    for c in codon_list:
        if c == 'UUU' or c == 'UUC':
            protein_list1.append('F')
            protein_list2.append('F')

        elif c == 'UUA' or c == 'UUG' or c == 'CUU' or c == 'CUC' or c == 'CUA' or c == 'CUG':
            protein_list1.append('L')
            protein_list2.append('L')

        elif c == 'UCU' or c == 'UCC' or c == 'UCA' or c == 'UCG' or c == 'AGU' or c == 'AGC':
            protein_list1.append('S')
            protein_list2.append('S')

        elif c == 'UAU' or c == 'UAC':
            protein_list1.append('Y')
            protein_list2.append('Y')

        elif c == 'UGU' or c == 'UGC':
            protein_list1.append('C')
            protein_list2.append('C')

        elif c == 'UGG':
            protein_list1.append('W')
            protein_list2.append('W')

        elif c == 'CCU' or c == 'CCC' or c == 'CCA' or c == 'CCG':
            protein_list1.append('P')
            protein_list2.append('P')

        elif c == 'CAU' or c == 'CAC':
            protein_list1.append('H')
            protein_list2.append('H')

        elif c == 'CAA' or c == 'CAG':
            protein_list1.append('Q')
            protein_list2.append('Q')

        elif c == 'AGA' or c == 'AGG' or c == 'CGU' or c == 'CGC' or c == 'CGA' or c == 'CGG':
            protein_list1.append('R')
            protein_list2.append('R')

        elif c == 'AUU' or c == 'AUC' or c == 'AUA':
            protein_list1.append('I')
            protein_list2.append('I')

        elif c == 'AUG':
            protein_list1.append('M')
            protein_list2.append('M')

        elif c == 'ACU' or c == 'ACC' or c == 'ACA' or c == 'ACG':
            protein_list1.append('T')
            protein_list2.append('T')

        elif c == 'AAU' or c == 'AAC':
            protein_list1.append('N')
            protein_list2.append('N')

        elif c == 'AAA' or c == 'AAG':
            protein_list1.append('K')
            protein_list2.append('K')

        elif c == 'GUU' or c == 'GUC' or c == 'GUA' or c == 'GUG':
            protein_list1.append('V')
            protein_list2.append('V')

        elif c == 'GCU' or c == 'GCC' or c == 'GCA' or c == 'GCG':
            protein_list1.append('A')
            protein_list2.append('A')

        elif c == 'GAU' or c == 'GAC':
            protein_list1.append('D')
            protein_list2.append('D')

        elif c == 'GAA' or c == 'GAG':
            protein_list1.append('E')
            protein_list2.append('E')

        elif c == 'GGU' or c == 'GGC' or c == 'GGA' or c == 'GGG':
            protein_list1.append('G')
            protein_list2.append('G')

        elif c == 'UAA' or c == 'UAG' or c == 'UGA':
            protein_list1.append('~')
            protein_list2.append('~')

        else:
            protein_list1.append('--Stray Nucleotide(s)--')
    # using created func. to convert protien list into str format
    final_answer = listToString(protein_list1)
    # returning list2 and amino acid sequence (str format)
    return protein_list2, final_answer


# initialising GUI
from tkinter import *
root = Tk()

Entry = Entry(root)
Entry.pack()

# for accessing data file and data
fHandle = input(Entry)
data_in_list_format = fHandle.readlines()
data_in_string = listToString(data_in_list_format)

# DNA to mRNA conversion if required
if 'T' in data_in_string:
    data_in_string = data_in_string.replace('T', 'U')
else:
    data_in_string = data_in_string

# returning a tuple with [0] = protein_list2 for counter operations and [1] = amino acid sequence
protein_seq = codonToProtein(data_in_string)

# measuring len parameters
amino_acid_seq = protein_seq[1]
len_of_pseq = len(amino_acid_seq)
len_of_nucleotides = len(data_in_string)

# length counter corrections
if amino_acid_seq[-1] == '-' and '~' in amino_acid_seq:
    len_of_pseq = len_of_pseq - 23                         # correcting '--Stray nucleotide(s)--'
    for x in amino_acid_seq:                               # correcting '~' stop codon
        if x == '~':
            len_of_pseq = len_of_pseq - 1
elif '~' in amino_acid_seq:
    for x in amino_acid_seq:
        if x == '~':
            len_of_pseq = len_of_pseq - 1
elif amino_acid_seq[-1] == '-':
    len_of_pseq = len_of_pseq - 23
else:
    len_of_pseq = len_of_pseq

# creating dict. for amino acid counter
amino_acids = protein_seq[0]
amino_acid_count = {}
for amino_acid in amino_acids:
    if amino_acid not in amino_acid_count:
        amino_acid_count[amino_acid] = 1
    else:
        amino_acid_count[amino_acid] = amino_acid_count[amino_acid] + 1

# final outputs
output_all = "Length of Inserted Nucleotides:" + len_of_nucleotides + "\nLength of Amino Acids:" + len_of_pseq + "\nAmino Acid Count:" + amino_acid_count + "\nConverted Protein Sequence:" + amino_acid_seq

def click():
    FilePath = Entry.get()

    Outbox = Entry(root, text=output_all)
    Outbox.pack()

button1 = Button(root, text="Transcribe/Translate", command=click)
button1.pack()



root.mainloop()














