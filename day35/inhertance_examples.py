#single

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Hey this is {self.name} and i can speak")

class child(person):
    def walk(self):
        print("Hey i can walk")

sapna = child("sapna", 23)
sapna.walk()
sapna.speak()
sapna.walk()

# Multiple

class Animal():
    def speak(self):
        print("I can speak")

class Dog():
    def run(self):
        print("Hey i can run")

class Puppy(Animal,Dog):
    def cry(self):
        print("Hey i can cry")


doggy = Puppy()
doggy.cry()
doggy.run()
doggy.speak()

#Multilevel

class Animal():
    def speak(self):
        print("I can speak")

class Dog(Animal):
    def run(self):
        print("Hey i can run")

class Puppy(Dog):
    def cry(self):
        print("Hey i can cry")


doggy = Puppy()
doggy.cry()
doggy.run()
doggy.speak()

#Hierarchial

class Animal():
    def speak(self):
        print("Hey i can speak"
              
            )
class Dog(Animal):
    def bark(self):
        print("woff woff")
    
class cat(Animal):
    def meow(self):
        print("Meow meow")

doggy = Dog()
doggy.bark()
doggy.speak()
# doggy.meow()
catty =cat()
catty.meow()
catty.speak()
