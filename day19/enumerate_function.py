'''
The enumerate function is a built-in function in python that allows you to
loop over a sequence(such as  a list, tuple and string) and get the index
and value of each element in the sequence at the same time.'''
students = ["Sapna", "Tanmay", "Tanisha", "Rahul", "Rohan", "Ranjitha", "Samanya", "Sanmitha", "Samiksha"]

marks = [76, 45, 34, 56, 78, 98, 65, 89]

for index, mark in enumerate(marks):
    print(f"The Student is {students[index]} and marks is {marks[index]}")


'''
The enumerate function returns a tuple containing the index and value of each element
in the sequence, you can use the for loop to unpack these tuples and assign them
to variables, as shown in example above

enumerate first is index and second is value
so always write index, value and not value, index if you write like this
value will have the index and index with have the value'''


'''
Changing the start index
By default the enumerate function starts with index 0, but you can specify 
a different starting index by passing it as argument
Say you dont want a 0-based indexing, instead want to start from 1 then you can use start = 1'''

for index, mark in enumerate(marks, start= 1):
    print(f"Roll No: {index} Student Name: {students[index]} Marks: {mark}")


fruits = ['apple', 'banana', 'papaya']
for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)