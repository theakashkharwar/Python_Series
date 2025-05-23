# Task : To Check if the no. is Prime or not

# Inititalize the num
num = int(input("Enter The No. : "))

# Create a loop to check for the no.
for i in range(2, num):
    if num % i == 0:
        flag = True
        break
    else:
        flag = False

# Declare the no. True Values
if flag == True:
    print("Its Not a prime No.")
else:
    print("Its a prime No.")
