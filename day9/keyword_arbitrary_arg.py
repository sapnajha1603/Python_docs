'''
While creating a function, pass a * before the parameter name while defining the function
The function accesses the arguments by processing them in the form of a dict.

In the below example *numbers will be seen as a tuple
'''

def average(*numbers):
    print(type(numbers))
    print(numbers)
    sum = 0
    for num in numbers:
        sum  = sum + num
    print(f"The average value is {sum/len(numbers)}")


average(4,5)
average(1,2,3,4,5)


def name(**name):
    print(type(name))

    print(f"{name['one']}")

name(one = "Sapna", two = "Tanmay", three = "Tanisha")
