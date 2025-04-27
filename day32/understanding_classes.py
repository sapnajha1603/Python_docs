'''
Create a simple class called Person with attributes name and age. 
Then create an object of this class and print the name and age attributes.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

obj1 = Person("Sapna", 24)
print(obj1.name)
print(obj1.age)


'''
Instance vs Class Variables

Define a class Car with a class variable number_of_wheels set to 4. 
Add an instance variable color in the __init__ method. Create two objects of the class Car with different colors.
Print the number_of_wheels and color for both objects.
Change the number_of_wheels for the Car class and see if it affects both objects.'''

class Car:
    number_of_wheels = 4
    def __init__(self, color):
        self.color = color

obj1 = Car("blue")
obj1.number_of_wheels = 10
print(f"The no of wheels are {obj1.number_of_wheels} and the color of the wheels are {obj1.color}")
obj2 = Car("green")
obj2.number_of_wheels = 3
print(f"The no of wheels are {obj2.number_of_wheels} and the color of the wheels are {obj2.color}")


'''
Manipulating Variables

Create a class Employee with instance variables name and salary.
Add a method to update the salary. Create an object of the class and update the salary using the method. 
Print the updated salary.'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def update_salary(self, new_salary):
        self.salary = new_salary

obj1 = Employee("Sapna", 7)
obj1.update_salary(8)

print(f"Name: {obj1.name} and salary: {obj1.salary} lpa")

'''
Constructor and Methods

Define a class Rectangle with instance variables length and width. 
Write an __init__ method to initialize these variables. 
Add methods to calculate the area and perimeter of the rectangle. 
Create an object and print its area and perimeter.'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


obj1 = Rectangle(5, 3)
print(obj1.area())
print(obj1.perimeter())

'''
Getters and Setters

Create a class Student with instance variables name and grade. 
Add getter and setter methods for these variables. 
Create an object of the class, set the name and grade using the setter methods, and print them using the getter methods.'''

class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        self._grade = new_grade


obj1 = Student("Sapna", "A")

print(obj1.name)
print(obj1.grade)

obj1.name = "Tanisha"
obj1.grade = "s"

print(obj1.name)
print(obj1.grade)

     

'''
Class Method and Static Method

Define a class Circle with a class variable pi set to 3.14. 
Add an instance variable radius in the __init__ method. 
Add a class method to update the value of pi. Add a static method to calculate the area of a circle given the radius. 
Create an object and calculate its area using the static method.
'''


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_pi(cls, new_pi):
        cls.pi = new_pi


    def area(new_radius):

        return  Circle.pi * new_radius ** 2

obj1 = Circle(4)
print(obj1.area(5))
obj1.set_pi(3.1452)
print(obj1.area(10))
