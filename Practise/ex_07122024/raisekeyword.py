"""
try:
    age = int(input("Enter your age:"))
    if age<0:
        raise ValueError
    print("You entered ",age)
except ValueError:
    print("Please enter valid age!!")  # passing message in except block
print("rest of the code")"""

try:
    age = int(input("Enter your age:"))
    if age<0:
        raise ValueError("Invalid age")
    print("You entered ",age)
except ValueError as var:
    print(var)
print("rest of the code")