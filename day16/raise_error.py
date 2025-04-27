'''
In python we can raise custom errors by using the raise keyword
We can raise built-in exceptions in python.
'''


a = input("\nEnter a number between 5 to 8: ")

if a == "quit":
    exit()

if a < 5 or a > 8:
    raise ValueError("Not a valid input")