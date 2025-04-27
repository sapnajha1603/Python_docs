'''
Sets are unordered collection of data items meaning we cant perform indexing or item assignement like set1[2] = 4, is not possible
They store multiple items in a  single variable. Set items are seperated by 
commas and enclosed within curly brackets{}.
Sets are unchangeable, meaning you cannot change items of the set once created.
Sets donot contain duplicate items.
'''
nums = {1,2,3,4,2,4,2,6,1,67}
print(nums)


name = {"Sapna", 1, 4 , 19, 13, True}
print(name)


# If you want to create an empty set, if you do {} then it will take it as dict, to create empty set u need to use new = set()
new = {}
print(type(new))

new2 = set()
print(type(new2))