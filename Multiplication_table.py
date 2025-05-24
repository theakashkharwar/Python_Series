# Task: Write a program to display multiplication table

# Ask for the no. whose table we have to Generate
num = int(input("Enter the no.: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

