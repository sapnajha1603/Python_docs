'''
Create a Person class with the following:

    Attributes: name, age
    A method greet that prints a message like: "Hello, my name is [name] and I am [age] years old."
    A method have_birthday that increases the person’s age by 1 and prints a message: "It's my birthday! I am now [new age] years old."

Once you've created the class, create an instance of the Person class and test both methods (greet and have_birthday).'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f" Hello, my name is {self.name} and I am {self.age} years old")
    
    def have_birthday(self):
        self.age = self.age + 1
        print(f" It's my birthday! I am now {self.age} years old")


Sapna = Person("Sapna", 24)
Sapna.greet()
Sapna.have_birthday()