# Mendel's First Law

# accessing data
fileHandle = open(input("Enter File Name Here: "))
data = fileHandle.readline().split()

# converting data into intergers and assigning values
k = int(data[0])
m = int(data[1])
n = int(data[2])

# assigning calculations for probability of all recessive alleles in offspring
total = k + m + n
P_m_m = (m/total) * ((m-1)/(total-1)) * (1/4)
P_m_n = (m/total) * (n/(total-1)) * (1/2)
P_n_m = (n/total) * (m/(total-1)) * (1/2)
P_n_n = (n/total) * ((n-1)/(total-1)) * (1)

# calculating probability of offspring not possessing a dominant allele (P_allRecessive) and possessing one or more (P_dominant)
P_allRecessive = P_n_n + P_n_m + P_m_n + P_m_m
P_dominant = 1 - P_allRecessive

# final answer
print(P_dominant)
