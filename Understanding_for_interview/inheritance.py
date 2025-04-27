class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")

class Hobby(Person):
    def hobby(self):
        print("My hobby is badminton")

sapna = Person("Sapna", 23)
sapna.info()
sapna_hobby = Hobby("Sapna", 23)
sapna_hobby.info()
sapna_hobby.hobby()