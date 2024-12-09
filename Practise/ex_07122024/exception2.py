num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
try:
    result = num1/num2
    print(reslt)
    #print(result)
#except (ZeroDivisionError, NameError): # to give both the exceptions in a single line
    #print("Something went wrong")

except (ZeroDivisionError, NameError) as obj: #to print the correct message
    print(obj)

finally:
    print("end of the code")