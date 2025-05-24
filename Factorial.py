# WAP a program to find factorial of a no. 

# User input of the no.
num = int(input("Enter the no.: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)