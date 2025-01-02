# for i in range(1,10):
#     if i==5:
#         break #when i becomes 5 it will exit the loop
#     print(i)
# print("Program Exited")

#continue will skip the step if condition is true and directly goes back to range step
# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

for i in range(1,10):
    if i==3 or i==5 or i==7:
        continue
    print(i)

for i in range(3,7,2):
    print(i)
