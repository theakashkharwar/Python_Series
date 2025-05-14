# Task: Show the month of the year

#Import Calender Module
import calendar

# Take the input of the year and month
Year = int(input("Tell me which year u want to see:\n "))
Month = int(input(f"Tell which month of the year {Year} u want to see:\n "))

Cal = calendar.month(Year, Month)

print(Cal)

