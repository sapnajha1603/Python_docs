'''
1. append
2. sort

U cant use sort to sort a list and assign to a diff list
list2 = list1.sort()
wont work , it will always give None
So if you want to use sort()
u will have to do this
list1.sort()
print(list1)
if u want to put in another list use sorted()
list2 = sorted(list1)

3. reverse
4. index
It will provide you the index of the given number
says list1 = [1,2,3,4]
print(list1.index(2))

5. count
It will provide the count of the element in the list
list3 = [1,2,3,1,1]
print(list3.count(1))

6. copy

7. insert used to inset value at a particular index

8. extend
This method adds an entire list or any other collection datatype
(set, tuple, dictionary) to the existing list

9. concatenating two lists
use + to concatenate two lists
'''

list1 = [3,2,1,4,5,5,7,5]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)

list12 = sorted(list(set(list1)))
print(f"The sorted list is : {list12}")

list10 = list(reversed(list1))
print(f"THE REVERSED OF LIST IS : {list10}")

list2 = [1,2,3,4]
print(list2.index(2))


list3 = [1,2,3,1,1]
print(list3.count(1))

#interesting understanding
l = [1,6,4,5,6]
m = l
m[0] = 4
print(l)

'''
We would think that l is not gonna get changed but to our surprise, 0th index of l also changes
Which means m is just a reference to l, the list will be the same, so if i manipulate m in any way, l will also get manipulated,
so instead of using m = l assignment , if you want to copy a list, use .copy()
'''


new = [5,7,7,8,5,4]
full_new = new.copy()
print("******************")
print(full_new)
full_new[3] = 564898
print(full_new)
print(new)
new.insert(1, 899)
print(new)


name1 = ["Hii My name is "]
name = ["Sapna"]
name1.extend(name)
print(name1)


list1 = [1,2,6,4,6,5]
list2 = [6,7,8,9,10]
list3 = list1 +list2
print(list3)

