"""def non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

input_word = input("Enter a Word:")
rep_char = non_repeating(input_word)
print(rep_char)"""


def set_non_rep(string):
    for char in set(string):
        if string.count(char) == 1:
            print(char)
            break
        else:
            print("No Unique character found")


input_set = input("Enter a set:")
set_non_rep(input_set)
