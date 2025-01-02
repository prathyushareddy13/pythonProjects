def vowel_count(string):
    vowel = "aeiou"
    count_vowel = 0
    #result ={} # declared a dict variable to store char as well
    for char in string:
        if char in vowel:
            count_vowel +=1
            #result[char] = count_vowel # storing char and count into result
    #print(result)
    print(count_vowel)

user_word = input("Enter a word:")
vowel_count(user_word)