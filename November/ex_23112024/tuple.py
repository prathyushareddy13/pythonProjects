#combining two tuples
grocery_list = ("Banana","Paneer","salt","Pepper")
household_list = ("TV","Fridge","Fans","Cooler")
combined_list = (grocery_list,household_list)
print(combined_list)
print(combined_list[1])
print(combined_list[0][2])

#to check if element is present in the tuple
print("Banana" in grocery_list)
print("Apple" in grocery_list)
print("AC" in household_list)

#can we modify the tuple?
#grocery_list[0] = "Apple" #we will get assignment error
