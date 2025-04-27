class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")

sapna = person("sapna", 24)
sapna.info()
Tanmay = person("Tanmay", 5)
Tanmay.info()