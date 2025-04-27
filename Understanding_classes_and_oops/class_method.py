'''
Create a class Animal with the following:

    A class attribute species = "Mammal".
    A class method set_species that allows you to change the value of the species attribute.
    Another class method get_species that prints the current value of species.

    First, call get_species to display the default species.
    Then, call set_species to change the species to "Reptile".
    Finally, call get_species again to display the updated species.

Remember to use the @classmethod decorator for both methods. Try coding it up, and I’ll review it!'''

class Animal:

    species = "Mammal"

    @classmethod
    def set_species(cls):
        cls.species = "Reptiles"

    @classmethod
    def get_species(cls):
        print(f"\nThe species selected is {cls.species}")

Animal.get_species()
Animal.set_species()
Animal.get_species()


