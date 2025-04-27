'''
Create a simple Car class with the following attributes and methods:

    Attributes: make, model, year
    Method: start_engine that prints "The engine is started."

Once you've created the class, create an instance of the Car class with specific values for make, model, and year. Call the start_engine method on the instance.

An additional attribute is_engine_on (initialize it to False in the constructor to represent that the engine is initially off).
Modify the start_engine method to set is_engine_on to True and print "Engine started" only if it's not already on. If the engine is already on, print "Engine is already running."
Add a new method stop_engine that sets is_engine_on to False and prints "Engine stopped."'''

class Car:

    def __init__(self, make, model, year, is_engine_on = False):
        self.make = make
        self.model = model
        self.year = year
        self.is_engine_on = is_engine_on
    def start_engine(self):
        if not(self.is_engine_on):
            self.is_engine_on = True
            print("Engine Started")
        else:
            print("Engine is already running.")

        print(f"The car is made by {self.make} and the model name is {self.model} and the year of manufacture is {self.year}")
    def stop_engine(self):
        if self.is_engine_on:
            self.is_engine_on = False
            print("Engine stopped.")  
        else:
            print("Engine is already off")     

hyundai = Car("Hyundai","Z1080",2023)
hyundai.start_engine()
hyundai.stop_engine()
hyundai.stop_engine()
