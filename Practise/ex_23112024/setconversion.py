#converting list to set
list1 = [45,2,3,67,89,34,6,8,3,2]
print(list1)
set1 = set(list1)
print(set1)

#tuple to set conversion
p = ("The Testing", "Academy", "The Testing")
print(set(p))

set2 = set(["The Testing","Academy","The Testing."])
set2.add("Prathyusha")
set2.add("Prathyusha") #even if we try to add same element twice set will consider only once
print(set2)
set2.remove("Prathyusha")
print(len(set2))

for i in set2: #no need to use rage keyword again
    print(i)
