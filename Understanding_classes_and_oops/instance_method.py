'''
Question 1: Instance Method

We’ve already covered instance methods (they use self). To reinforce this, create a simple class called Dog 
with attributes name and breed. Add an instance method called bark that prints "Woof!". 
Then create an instance of Dog and call the bark method.'''

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"\nHii My name is {self.name} and my breed is {self.breed} and Woof!!!!!!!!!!")

Oggy = Dog("Oggy", "Poodle")
Oggy.bark()
