"""for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()"""

"""for i in range(5,1,-1):
    for j in range(1, i - 1):
        print(j, end=" ")
    print()"""

def left_triangle(number):
    for i in range(1, number+1):
        space = " " * (number - i)
        reverse_string=""
        for j in range(i,0,-1):
            reverse_string = reverse_string+str(j)
        print(space+reverse_string)

input1= int(input("Enter a number:"))
left_triangle(input1)

"""def left_triangle1(number):
    for i in range(1, number+1):
        space = " " *(number-i)
        reverse_string = ""
        for j in range(1,i):
            reverse_string = reverse_string + str(j)
        print(space + reverse_string)

inputL= int(input("Enter a number:"))
left_triangle1(inputL)"""





