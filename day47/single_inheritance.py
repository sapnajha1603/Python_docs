class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, species="Cat")
        self.age = age
        
    def make_love(self):
        print(f"I love Pizzas and lasagnan and my age is {self.age}")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

c = Cat("Cat", 2)
c.age = 4
c.make_love()
# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat

