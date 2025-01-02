dict1 = { "a" : 10, "b" : 13, "c" :15}
dict2 = {"d": 14, "b": 16, "e" :1}

dict3 = dict1 |dict2 # if key is same it will keep the right side dict values(dict2 here)
print(dict3)

dict1.update((dict2)) # it will update dict2 values to dict1
print(dict1)

missing_key = set(dict1.keys()) - set(dict2.keys())
print(missing_key)

