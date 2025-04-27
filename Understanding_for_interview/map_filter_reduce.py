from functools import reduce

list1 = [2,3,4,5,6,7,8]

list2 = list(map(lambda x:x*2, list1))
print(f"The squares of values using map is: {list2}")


list3 = list(filter(lambda x:x%2==0, list1))
print(f"The even numbers are: {list3}")

list4 = reduce(lambda x,y: x+y, list1)
print(f"The total sum is : {list4}")