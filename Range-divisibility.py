# Task: Print all Numbers in a Range Divisible by a Given Number

Upper_Limit = int(input("Enter the Upper Limit of the range: "))
Lower_Limit = int(input("Enter the Lower Limit of the range: "))

Divisor = int(input("Enter the divisor: "))
for i in range(Upper_Limit, Lower_Limit + 1):
    if i % Divisor == 0:
        print(i)

        
