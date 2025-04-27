'''
Lists are ordered collection of data items
They store multiple items in a single variable
List items are seperated by commas and enclosed within square brackets
Lists are changeable meaning we can alter them after creation

LISTS CAN BE CHANGED BY APPENDING DATA BUT WE CAN'T APPEND DATA IN A TUPLE
'''


if "Sa" in "Sapna":
    print("Yes")
else:
    print("No")

list1 = [1,2,3,4,5,6,"Sapna","Jha", True, "Tanmay", "Tanisha"]
print(list1)
print(list1[1:9])
print(list1[1:9:1])
print(list1[1:9:2])

list2 = [i for i in range(10)]
print(list2)