'''
In Python, the primary types of methods you will encounter in classes are:

    Instance Methods
    Class Methods
    Static Methods

However, there are other special methods that can be defined within a class, known as "magic methods"
or "dunder methods" (because they have double underscores before and after their names). 
Here is an overview of these methods:'''



'''
A static method is defined using the @staticmethod decorator. 
It does not take a self or cls parameter and does not depend on the instance or class variables. 
Static methods are used for utility functions that perform tasks in isolation.
'''

class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        # Perform some task
        return arg1 + arg2

# Usage
result = MyClass.static_method(5, 3)
print(f"The result is: {result}")  # Output: 8

'''
A class method is defined using the @classmethod decorator. 
It takes cls as the first parameter, which refers to the class itself. 
Class methods can access and modify class variables, but not instance variables.'''

class MyClass:
    class_variable = 0

    @classmethod
    def class_method(cls, increment):
        # Modify class variable
        cls.class_variable += increment
        return cls.class_variable

# Usage
MyClass.class_method(5)
print(MyClass.class_variable)  # Output: 5

'''
Instance Methods

    Definition: Methods that operate on an instance of the class.
    Parameter: self
    Access: Can access and modify instance variables and class variables.
'''

class MyClass:
    def instance_method(self):
        print("This is an instance method.")
