#Calculator Assignment
print("Welcome to my Calculator")
print(" ")

sign = int(input('''Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\n'''))

Number_1 = int(input("Enter the first Number: "))
Number_2 = int(input("Enter the second Number: "))

if sign == 1:
    print(f"The addition of {Number_1} and {Number_2} is ", Number_1 + Number_2)
elif sign == 2:
    print(f"The subtraction of {Number_1} and {Number_2} is ", Number_1 - Number_2)
elif sign == 3:
    print(f"The Multiplication of {Number_1} and {Number_2} is ", Number_1 * Number_2)
elif sign == 4:
    if Number_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The division of {Number_1} and {Number_2} is ", Number_1 / Number_2)

print("Thanks for using this Calculator")
print("Bye")