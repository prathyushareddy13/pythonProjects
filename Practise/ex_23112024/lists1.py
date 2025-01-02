mylist = ["Apple","Banana","Cherry","Plum","Mango","Grapes"]
print(mylist[1]) #banana
print(mylist[-2]) #Mango

# Range of indexes
print(mylist[2:5]) #['Cherry', 'Plum', 'Mango']
print(mylist[-5:-1]) #['Banana', 'Cherry', 'Plum', 'Mango']

#changing the value
mylist[1] = "Blue Berry"
print(mylist) #['Apple', 'Blue Berry', 'Cherry', 'Plum', 'Mango', 'Grapes']

#loop for a list
for i in mylist:
    print(i)

#to check if an element is present in a list
if "Apple" in mylist:
    print("yes")
else:
    print("no")

#to know the length
print(len(mylist)) #6