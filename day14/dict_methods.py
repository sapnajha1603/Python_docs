'''
Sets are unordered
But dictionaries from Python 3.7 have become ordered(means if you give dict like {1:'Sapna', 2:'Tanmay', 3:'Tanisha})
Then it will print it in the same way {1:'Sapna', 2:'Tanmay', 3:'Tanisha}
But say u have a  set with data {1,5,35,3,5,2}
Then it can print it like this {1,5,35,3,2} or {1,2,3,5,35} or anything else as well'''

'''
Update - The update() method updates thee value of the key provided if the 
item already exists in the dictionary, else it creates a new key-value pair'''

info = {'Name': 'Sapna', 'age': 24, 'eligible': True}
info2 = {'Company': 'Bosch'}
print(info)

info.update({'age': 25})
info.update({'DOB' : 2001})
info.update(info2)
print(info)

'''
Clear method is used to clean the entire dict out'''
# info.clear()
# print(info)

'''
The pop() method removes the key-value pair whose key is passed
as a parameter'''

info.pop('DOB')
print(info)

'''
popitem() method removes the last key-value pair from the dictionary'''

info.popitem()
print(info)


'''
del the entire dict
'''

del info['age'] #Used to delete a key-value pair from the dict
print(info)

# del info #Used to delete the entire dict
# print(info)

