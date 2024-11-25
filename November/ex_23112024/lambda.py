def add_num(a,b):
    return a+b

lambda_res1 = lambda a,b:a+b
print(lambda_res1(3,5))

result1 = lambda a: a**3
print(result1(2))

#n = input("Enter a number:")
result2 = lambda n: "Even" if n%2==0 else "Odd"
print(result2(4))


#even_odd = lambda : "Even" if (int(input("enter a number:"))%2 ==0) else "Odd"
#print(even_odd)