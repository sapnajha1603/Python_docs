'''

Tuples are ordered collection of data items.
They store multiple items in a single variable.
Tuple items are seperated by commas and enclosed within round brackets ()
Types are unchangeable meaning we can not alter them after creation
The only diff between list and tuple is tuple is unchangeable

TUPLES ARE IMMUTABLE
STRINGS ARE IMMUTABLE
LISTS ARE MUTABLE
SETS ARE MUTABLE
'''

tup1 = (1,2,3)
print(type(tup1), tup1)

tup2 = (1,2)
print(type(tup2), tup2)

tup3 = (1)
print(type(tup3), tup3) #for tuple of 1 object, python idenitifies it as integer type, so if u want to define a tuple with only one element use (1,)

tup4 = (1,)
print(type(tup4), tup4)

#You can assign multiple data types in a tuple as well, like we do for lists

tup5 = (1,2,3, "Sapna", "Jha", True)
print(tup5)