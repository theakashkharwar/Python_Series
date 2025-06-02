# Task: Print a Narcissit Number.

# Theory: A no. is Narcissit number if the no. is equal to the sum of its digits raised to the power of its no. of digits
#           Ex -> 153 = 1^3 + 5^3 + 3^3



# Define the Interval
StartNo = int(input("Enter the starting Interval: "))
LastNO = int(input("Enter the Last Interval: "))

# Create a loop for no. to i terate between the loop
for i in range(StartNo, LastNO):
    order = len(str(i))
    num = i
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit**order
        num //= 10

    if i == sum: # Check for Narcissit No.
        print(i)