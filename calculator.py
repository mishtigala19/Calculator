# Author: Mishti Gala
# Email: mishtikalpes@umass.edu
# Date: 1st November 2023

# This is the main loop of the calculator, which allows the user to perform multiple calculations until they choose to exit.
while True:
    
    # Display the available operations to the user.
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter q or Q to Exit")

    # Prompt the user to enter their choice.
    choice = input("Enter your choice: ")

    # Check if the user wants to exit the calculator.
    if choice == 'q' or choice == 'Q':
        break

    # Prompt the user to enter two numbers for the selected operation.
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    # Based on the user's choice, perform the corresponding operation and display the result.
    if choice == "1":
        print(num1, "+", num2, "=", (num1 + num2))
    elif choice == "2":
        print(num1, "-", num2, "=", (num1 - num2))
    elif choice == "3":
        print(num1, "*", num2, "=", (num1 * num2))
    elif choice == "4":
        # Check if the user is attempting to divide by zero.
        if num2 == 0.0:
            print("Divide by 0 Error")
        else:
            # Perform the division operation and display the result.
            print(num1, "/", num2, "=", (num1 / num2))
    else:
        # If the user's choice is not a valid option, inform them of the invalid choice.
        print("Invalid Choice")
