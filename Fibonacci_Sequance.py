# Task: Generate a fibonacci Series

# Specify the no. of the terms
nterms = int(input("Enter the term upto which u want to print fibonacci series: "))

# Specify the starting terms
n1, n2 = 0, 1
count = 0

# Check if the nterms are valid or not
if nterms < 0:
    print("Print Positive no. of terms.")

# if there are only one terms
elif nterms == 1:
    print(n1)

# print the seriec
elif nterms > 2:
    while count < nterms:
        print(n1)
        nth = n1 + n2
        
        # update n1 and n2
        n1 = n2
        n2 = nth
        count += 1
