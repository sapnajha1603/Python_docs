'''
Whenever string literals are present just after the definition of a function,
module, class or a method, they are associated with the object ad their doc attribute
We can later use this attribute to retrieve this doc string

'''

def square(n):
    '''
    Takes in a number n, returns the square of n
    '''
    print(f"The square of {n} is {n**2}")

square(2)
print(square.__doc__)