#Tuple to list
items_tuple = ("Covers","bags","biscuits","Chocos","curd")
print(items_tuple)
items_list = list(items_tuple)
print(items_list)
items_list[2] = "Cake"
items_list.remove("Chocos")
items_list.pop()
print(items_list)

#list to tuple
car_list = ["Hyundai","Kia","Honda","Audi","BMW"]
print(car_list)
car_tuple = tuple(car_list)
print(car_tuple)
#car_tuple.pop()
#car_tuple.add("Lambo")