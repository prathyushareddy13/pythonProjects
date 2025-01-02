input1 = float(input("Enter first number:"))
input2 = float(input("Enter Second number:"))
input3 = float(input("Enter Third number:"))

if(input1 >= input2) and (input1 >= input3):
    greater = input1
elif(input2 >= input1) and (input2 >= input3):
    greater = input2
else:
    greater = input3

print("The greater number of all three numbers is:", greater)