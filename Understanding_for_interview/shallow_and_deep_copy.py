list1 = [1,2,4,3,5,6,4,9,[4,5]]

list2 = list1.copy() # Shallow copy

# list2[8][0] = 567
# print(list2)
# print(list1)

#deep copy
import copy

list3 = copy.deepcopy(list1)
list3[8][0] = 567
print(list3)
print(list1)
