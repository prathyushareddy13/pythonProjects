input_side1 = int(input("Enter the value of side1:"))
input_side2 = int(input("Enter the value of side2:"))
input_side3 = int(input("Enter the value of side3:"))

if input_side1 == input_side2 and input_side1 == input_side3:
    print("It is an Equilateral Triangle")
elif input_side1 == input_side2 or input_side1 == input_side3 or input_side2 == input_side3:
    print("It is an Isosceles Triangle")
else:
    print("It is a Scalene Triangle")