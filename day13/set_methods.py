'''
Union   method prints all the items that are present in both the sets
The union() method returns a new set .
'''

s1 ={3,5,6,7}
s2 = {8,9,6}

print(s1.union(s2))

s3 = s1.union(s2)
print(s3)


'''
Update() method adds items into existing set from another set
'''

s4 = {7,4,3,5,2}
s5 ={8,6,9}
s4.update(s5)
print(s4)

'''
Intersection method prints only items that are similar to both the sets
The intersection() method returns a new set
'''

s6 = {1,2,3,4,5}
s7 = {3,4,7}
print(s6.intersection(s7))

'''
Intersection_update method will update the existing set with only similar values 
from the other set'''

s8 = {1,2,3,4,5}
s9 = {3,4,7}
s8.intersection_update(s9)
print(s8)

'''
Symmetric difference method prints only items that are not similar
to both the sets. The symmetric method returns a new set whereas symmetric_difference_update
method updates into the existing set from another set'''


states1 = {"Karnataka", "AP", "UP", "Maharashtra", "Gujurat"}
states2 = {"Karnataka", "AP", "Kerela", "MP", "Gujurat", "Tamil Nadu"}


print(states1.symmetric_difference(states2))

states1.symmetric_difference_update(states2)
print(states1)

'''
differece() and difference_update() prints only items that are only present in the
original set and not in both the sets.
The difference() method returns a new set whereas difference_update() updates 
the existing set from another set'''


names1 = {"Sapna", "Tanmay", "Tani", "Taylor Swift", "Kriti Sanon"}
names2 = {"Sapna", "Tanmay", "Tani"}

print(names1.difference(names2))
names1.difference_update(names2)
print(names1)

'''
The isdisjoint() method checks if items of given set are present in another set.
This method returns false if items are present, else it returns True
'''

num1 = {1,2,3,4,5}
num2 = {5,6,7,8}
num3 = {9}
print(num1.isdisjoint(num2))
print(num1.isdisjoint(num3))

'''
issuperset() method checks if all the items of a particular set are present
in the original set. It returns True if all the items are present, else it returns False
'''

countries = {"India", "Japan", "Germany", "Tokyo", "USA", "SA", "Bangladesh", "Nepal", "Bhutan", "Bangkok", "South Korea"}
asian_county = {"India", "Japan", "South Korea"}

print(countries.issuperset(asian_county))

countries.issuperset(asian_county)
print(countries)


'''
The issubset() method checks if all items of the original set are present in 
the particular set. It returns True if all the items are present, else it
returns False
'''
countries1 = {"India", "Japan", "Germany", "Tokyo", "USA", "SA", "Bangladesh", "Nepal", "Bhutan", "Bangkok", "South Korea"}
asian_county = {"India", "Japan", "South Korea"}
print(asian_county.issubset(countries))
countries.issubset(asian_county)
print(countries)

'''
add method
'''

num1 = {1,2,3,4,5}
num2 = {6,7,8,9,10}

num1.add(21)
print(num1)

# If i want to add the entire num2 to num1 i should use update ()

num1.update(num2)
print(num1)

'''
remove / discard
The main difference between remove and discaed is that, if we try to delete and
element which is not present in set, then remove() raises and error, wheread
discard() does not raise any error'''

num1.remove(21)
print(num1)
# num1.remove(4555)
num1.discard(4555)
num1.add(4555)
print(num1)
num1.discard(4555)
print(num1)

'''
pop method removes the last item of the set, but the catch is that we dont 
know which ite gets popped as sets are unodered. However you can access the
popped items if you assign the pop() method to a variable'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)


'''
del - delete'''

nums23 = {4,6,6,74,78}
print(nums23)
del(nums23)
# print(nums23)

'''
clear is used to clear all items in the set and prints an empty set'''

num13 = {1,23,56,642,466}
print(num13)
num13.clear()
print(num13)