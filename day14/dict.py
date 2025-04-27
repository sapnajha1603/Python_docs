'''
Dictionaries are ordered collection of data items.
They store multiple items in a single variable.
Dictionary items are key-value pairs that are seperated by commas
and enclosed within curly brackets{}'''

info = {'Name': 'Sapna', 'age': 24, 'eligible': True}
print(info)

#To access a single value

'''
The only difference between directly giving dict_name[key] and dict_name.get(key) is if the key isn't present then it throughs an error
but when you use .get() method, if the key isn't present it will just print None'''
print(info['Name'])
print(info.get('Name'))

# print(info['Name2'])
print(info.get('Name2'))

'''
To print keys and values '''

print(info.keys())
print(info.values())
print(info) #Prints the dict
print(info.items()) #Prints the dict items in (key, value) pairs


#Using for loop
for key,value in info.items():
    print(f"The value corresponding to {key} is {value}")