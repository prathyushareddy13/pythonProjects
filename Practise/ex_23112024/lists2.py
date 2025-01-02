from Practise.ex_23112024.lists1 import mylist

#append
mylist.append("Orange")
print(mylist) #['Apple', 'Blue Berry', 'Cherry', 'Plum', 'Mango', 'Grapes', 'Orange']

mylist.insert(3,"Dragon Fruit")
print(mylist) #['Apple', 'Blue Berry', 'Cherry', 'Dragon Fruit', 'Plum', 'Mango', 'Grapes', 'Orange']

#to remove an item - pop()
mylist.pop(0)
print(mylist) #['Blue Berry', 'Cherry', 'Dragon Fruit', 'Plum', 'Mango', 'Grapes', 'Orange']

#del keyword
del mylist[2]
print(mylist) #['Blue Berry', 'Cherry', 'Plum', 'Mango', 'Grapes', 'Orange']

#clear()
mylist.clear() # it will clear all the items

#to copy a list
mylist1 = list(mylist)
mylist2 = mylist.copy()