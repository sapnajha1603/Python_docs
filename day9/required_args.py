'''
In case we don't pass the argument with key =  value syntax, then it is 
necassary to pass the arguments in the correct positional order and the no. o  
arguments passed should match with actual func def
'''

def average(a, b): #Even if i provide arguments value here, if i have provided values in the func call, it will take those values
    average = (a+b)/2
    print(f"\nThe average of {a} and {b} is {average}")


#Test cases
average()