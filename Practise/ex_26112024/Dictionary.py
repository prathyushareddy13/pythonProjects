my_dict = {
    "name": "Prathyusha",
    "age": 35,
    "role": "Engineer"
}

#print(my_dict["age"])

my_dict["age"] = 32
print(my_dict["age"])
del my_dict["role"]
print(my_dict)

print("role" in my_dict)
print("age" in my_dict)

for key,value in my_dict.items():
    print(key, "-->", value)