
def char_freq(string):
    char_count={}
    for char in string:
        char_count[char] = char_count.get(char,0)+1
    print(char_count)

user_input = input("Enter a string:")
char_freq(user_input)
