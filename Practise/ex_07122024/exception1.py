num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
try:
    result = num1/num2
    #print(result)
except ZeroDivisionError:
    print("Division with zero is not possible")
except NameError: # to handle incorrect variable names
    print("Please check the variable names")
else:
    print(result)
    #print(reslt) # variable name is incorrect
finally:
    print("end of the code")