# Task: To check if a no. is leap year or not

# Enter the Year
year = int(input("Enter the year: \n"))

# Conditions for a year to be leap year

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")


