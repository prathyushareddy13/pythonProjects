set1={"Ani","Anu","Ball","Ani"}
set2 = {"Ani","Ball","Bat", "Line"}
# union
union_set = set1.union(set2)
print(union_set)
#intersection
inter_set = set1.intersection(set2)
print(inter_set)

#difference
diff_set = set1.difference(set2) #different items in 1st set will be printed
print(diff_set)

diff_set2 = set2.difference(set1) #set 2 different items will be printed
print(diff_set2)