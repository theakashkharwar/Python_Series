#Task:  Quaratic_Equations

# Enter the Coefficiants 
a = float(input("Enter the coefficiant a: \n"))
b = float(input("Enter the Coefficiant b: \n"))
c = float(input("Enter the coefficiant c: \n"))

# Print the equation
print(f"The quadratic equation is: {a}x^2 + {b}x + {c} = 0")

# Value of the Root is
root_1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
root_2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

# Print the value of the roots
print(f"Value of the first root is {root_1}")
print(f"Value of the Second root is {root_2}")

