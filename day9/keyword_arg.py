
'''
We can provide arguments with key =  value, this way the interpreter recognizes
the arguments by the parameter name. Hence the order in which the arguments 
are passed does not matter
'''

def average(a = 10, b = 6): #Even if i provide arguments value here, if i have provided values in the func call, it will take those values, here a=10 and b=6 are default arguments
    average = (a+b)/2
    print(f"\nThe average of {a} and {b} is {average}")


#Test cases
average(b = 20, a = 10)
