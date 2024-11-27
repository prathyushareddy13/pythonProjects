
dup_dict = {"a":4, "b":3,"c":6,"d":4,"e":3}
dict_set = set(dup_dict.values())
print(dict_set)

unique_value = set()
result_dict = {}
for key,value in dup_dict.items():
    if value not in unique_value:
        unique_value.add(value)
        result_dict[key] = value
print(result_dict)

