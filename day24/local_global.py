'''
A variable is a named location in memory that stores a value.
In Python, we can assign values to variables using the assignment operator =. For example:
 
x = 5
y = "Hello, World!"

A local variable is a variable that is defined within a function and is only accessible within that function. 
It is created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is 
accessible from within any function in your code.

'''


x = 10


def hello():
    x = 5
    print(f"The local value of x is : {x}")
print(f"The global value of x is : {x}")
hello()
print(f"The global value of x is : {x}")


'''
Now if u want to change the value of x globally u need to modify the global variable x, for that we use the global keyword
'''

y = 10045990


def global_try():
    global y
    y = 590876
    print(f"The local value of y is : {y}")
print(f"The global value of y is : {y}")
global_try()
print(f"The global value of y is : {y}")


'''
It's important to note that it's generally considered good practice to avoid modifying global variables
 from within functions, as it can lead to unexpected behavior and make your code harder to debug.

'''