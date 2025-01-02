def find_smallest(a, b, c):
    if (a <= b) and (a <= c):
        result = a
    elif (b <= a) and (b <= c):
        result = b
    else:
        result = c
    return result


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
# res = find_smallest(a,b,c)
# print(find_smallest(10,3,1))
print("The smallest number is:", find_smallest(a, b, c))
