#substring functions

# string1 = "Welcome to Python"
#
# print(string1.endswith("come"))
# print(string1.endswith("thon"))
# print(string1.startswith("Wel"))
# print(string1.startswith("Python"))
# print(string1.find("come"))
# print((string1.find("Prat"))) # if not found it will return -1
# print(string1.count("o")) #no.of occurrences of a char

#converting functions
s5 = ("hello how are you doing?"
      "i am doing good")
print(s5.capitalize()) #Hello how are you doing?i am doing good. Only first letter will be capitalized
print(s5.title())  #Hello How Are You Doing?I Am Doing Good. All the first letters of each word will be capitalized
print(s5.lower())  #hello how are you doing?i am doing good
print(s5.upper())  #HELLO HOW ARE YOU DOING?I AM DOING GOOD

s6 = "Hello, How Are You?"
print(s6.swapcase())  #hELLO, hOW aRE yOU? Swaps upper to lower and lower to upper
print(s5.replace("are you","you are")) #hello how you are doing?i am doing good

