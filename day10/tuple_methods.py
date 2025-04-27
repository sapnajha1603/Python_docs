'''
Tuples are immutable, hence if you want to add, remove or change tuple iterms,
first you must convert the tuple into a list
Then perform operation on that list and convert it back to tuple

1. Concatenation of two tuples are possible
2. count
3. index
tuple.index(element, start, end)
4. len() to print length of tuple
'''

tup1 = (1,2,2,2,23)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3)
print(f"The count of 2 is : {tup3.count(2)}")
print(f"The length of the tuple is : {len(tup3)}")


tup4 = (4,5,3,6,4,6,5,4)
res = tup4.index(4,1,6)
print(res)

