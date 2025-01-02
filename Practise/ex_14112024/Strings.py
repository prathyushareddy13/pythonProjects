#string declaration
# string="Welcome"
# s1='Welcome'
# s2=str("welcome")
# s3=str('Welcome')
from curses.ascii import isdigit

# #creating an empty string
# name=""
# name1=''
# name2=str()

#memory allocation - every time when we reassign the variable id changes
# print(id(string))  #id is 2023141718896
# string="Hello Prathyusha"
# print(id(string))  # 1710735899824

#string slicing
s="Hello World"

# print(s[2:5])
# print(s[1:3])
# print(s[2:])
# print(s[:4])
# print(s[:-1]) #skips last one char
# print(s[:-3]) #skips last 3 chars
# print(s[::2]) #skips one char in between
# print(s[::3]) #skips 2 char n between
# print(s[::-1]) #to reverse the string

#ord and chr functions
# print(ord("A")) #prints ASCII value of a char
# print(chr(69)) #prints char of the given ASCII value

#max, min, len of a string
# print(max("abc")) #based on ascii value it will print the max value char
# print(min("def")) #based on ascii value it will print the min value char
# print(len(s))

#String functions
inp = "welcome to Python"
print(inp.isalnum())
print("HelloWorld".isalpha()) #if there are spaces in the string it is giving false
#print("Hello",isdigit())
print("first number".isidentifier())
print(" ".isspace())