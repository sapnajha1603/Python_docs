Constructors

A constructor is a special method in a class used to create and initialize an object of a class.
There are different types of constructors.
Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class.

The main purpose of a constructor is to initialize or assign values
to the data members of that class.

It cannot return any value other than None


Syntax of python constructor

def __init__(self):
    #Initialization

init is one of the reserved functions in python
In OOPs, it is known as a constructor. 
We can also create constructor by defining the function name with same class name.

Type of constructors in python

1. Parameterized Constructor

2. Default constructor

Parameterized constructor in python

When the constructor accepts arguments along with self, it is known as parameterized constructor.

These arguments can be used inside the class to assign the values to the data members.

Example

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group =  group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

O/P

Crab belongs to the Crustaceans group

Default constructor in Python

When the constructor doesn't accept any arguments from the object and has only one parameter, self, in the constructor, it is known as Default constructor.

Example
class Details:
    def __init__(self):
        print("Animal crab belongs to Crustaceans group")

obj1 = Details()
O/P

Animal Crab belongs to Crustaceans group