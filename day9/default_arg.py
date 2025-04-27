def average(a = 10, b = 6): #Even if i provide arguments value here, if i have provided values in the func call, it will take those values, these are the default arguments
    average = (a+b)/2
    print(f"\nThe average of {a} and {b} is {average}")


#Test cases
average(3,6) #Provide the values #3 and 6 are actual arguments
average() #will take the default values given in func def
average(1) #will take a = 1 and b = 6
average(b = 10) #will take a as 1 and b as 10
