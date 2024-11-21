input1 = int(input("Enter the first number:"))
input2 = int(input("Enter the second number:"))
#input3 = int(input("Enter the third number:"))

def _sum(num1=10,num2=20,num3=30):
    result = num1+num2+num3
    return result

res= _sum(input1,input2,5)
print(f"The sum of 3 numbers is: {res}")