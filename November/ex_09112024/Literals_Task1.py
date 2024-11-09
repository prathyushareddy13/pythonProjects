try:
    # Getting three inputs from user
    input1 = int(input("Enter the first number:"))
    input2 = int(input("Enter the second number:"))
    input3 = int(input("Enter the third number:"))

    # adding the inputs and storing them in a variable and printing the output
    addition = input1 + input2 + input3
    print("Sum of the numbers:\t", addition)

    # subtracting the inputs and storing them in a variable
    # printing the output
    subtraction = (input1 - input2) - input3
    print("Subtraction of the numbers:\t", subtraction)

    """ multiplying the inputs and storing them in a variable
    printing the outputs """
    multiplication = input1 * input2 * input3
    print("Multiplication of the numbers:\t", multiplication)

    """ dividing the inputs and storing them in a variable
     printing the outputs"""
    division = ((input1 / input2) / input3)
    print("Division of the numbers:\t", division)

# Handling exception if there is an input as 0
except ZeroDivisionError:
    # Printing the alert message
    print("Please provide input value greater than Zero")

# Handling exception for non integer inputs
except:
    # printing an informative message to change the input
    print("Input is not a number, Please try again")
