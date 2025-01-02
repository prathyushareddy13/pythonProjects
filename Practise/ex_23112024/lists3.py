#combine /join lists
list1 = ['a','b','c']
list2 = [1,2,3]
# list3 = list1+list2
# print(list3)

#using loop
# for i in list2:
#     list1.append(i)
# print(list1)

#using extend()
list1.extend(list2)
print(list1)