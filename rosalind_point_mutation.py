# Counting Point Mutation

# accessing data
fileHandle = open(input("Enter File Name Here: "), 'r')
Data = fileHandle.readlines()

# defining counting point mutation func.
def cnt_mutation(s, t):
    # assigning variables for range func.
    x = min(len(s), len(t))              # len(s) == len(t)
    result = abs(len(s) - len(t))        # priming 'result' value to 0
    # setting up counter
    for i in range(0, x):
        if s[i] != t[i]:
            result = result + 1
    return result

# setting variables s and t to the given sequences in the data
s = Data[0]
t = Data[1]

# final answer
print(cnt_mutation(s, t))
