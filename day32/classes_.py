class Person():
    Name = "Sapna"
    Age = 24
    Occupation = "Engineer"
    def info(self):
        print(f"My name is {self.Name} and my occupation is {self.Occupation}")

object1 = Person()
# print(f"Name: {object1.Name} and Occupation : {object1.Occupation}")
object1.info()

object2 = Person()
object2.Name = "Tanisha"
object2.Occupation = "Being cute"
# print(f"Name: {object2.Name} and Occupation : {object2.Occupation}")

object2.info()
