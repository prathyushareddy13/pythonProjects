class FiveDivsionError(Exception):
    def __init__(self):
        print("you cannot divide by 5")
        pass
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    if num2==5:
        raise FiveDivsionError
    div = num1/num2
    print(div)
except (FiveDivsionError,ZeroDivisionError) as var:
    print(var)
finally:
    print("End of the code")