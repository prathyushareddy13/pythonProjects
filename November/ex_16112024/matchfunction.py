input_symbol = input("Enter the Operator:")

match input_symbol:
    case "+":
        print("It is an addition")
    case "-":
        print("It is a subtraction")
    case "*":
        print("It is a Multiplication")
    case "/":
        print("It is a division")
    case _:
        print("Please provide valid input")