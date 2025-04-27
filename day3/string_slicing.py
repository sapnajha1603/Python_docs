names = "Sapna, Tanmay, Tanisha"
fruit = "Mango"
print(f"The length of the string is : {len(names)}")

#slicing operations
print(names[0:5])
print(names[1:5])
print(names[1:]) #Then it will take end element as len(names)
print(names[:5]) #Then it is going to start from 0 itself
print(names[:]) #Then it is going to start from 0 itself and it will take end element as len(names)
print(names[:-1])  #Then the code will manipulate it as names[: len(names) - 1] len is 22 so 22-1 is 21 , so it will go from 0 to last but 1 element
print(names[18 : -1])   #from 18 to 21
print(fruit[-3 : -1]) #This will be manipulated as names[len(fruit)-3 : len(fruit)-1] 2:4

nm = "Harry"
print(nm[-4:-2])