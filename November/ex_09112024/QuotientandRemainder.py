import math

try:
    # Accept Dividend from user
    nDividend = int(input("Enter Dividend:"))

    # Accept Divisor from user
    nDivisor = int(input("Enter Divisor:"))

    # Computing quotient by dividing Dividend and Divisor
    nQuotient = math.floor(nDividend / nDivisor)

    # Remainder is computed by getting the mod of Dividend and Divisor
    nRemainder = nDividend % nDivisor

    # Print the Quotient and Remainder
    print("Quotient is:", nQuotient,"\nRemainder is:",nRemainder)

except ZeroDivisionError:
    # Handling exception when nDivisor is passed as 0
    print("You can't divide by zero!")
except:

    # Handling exception when inputs are not a number
    print("Input perhaps not a number!")

