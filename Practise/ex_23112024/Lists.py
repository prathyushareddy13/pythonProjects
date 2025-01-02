my_list = ["Prathyusha","Rakesh","Sid","Sai","Mum","Dad"]
#print(my_list)
#print(my_list[2])
my_list.insert(3,"Doll")
#print(my_list)
my_list.extend(["Apple","Mango","Plum"])
print(my_list)

my_list[0] = "Prat"
print(my_list)

del my_list[7]
print(my_list)

my_list.remove("Plum")
print(my_list)

my_list.pop()
print(my_list)

my_list1 = [2,5,8,3,2,1,9]
my_list1.extend([3,5,7])
my_list1.remove(3)
my_list1[5] = 11
print(my_list1)