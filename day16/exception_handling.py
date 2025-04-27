'''
Exception handling is the process of responding to unwanted and unexpected
events when a computer program runs.
Exception handling deals with these events to avoid the program or system crashing
and without this process, exceptions would disrupt the normal operations of a 
program

Exceptions in python
Python has many built-in exceptions that are raised when your program
encounters an error(something in the program goes wrong)

1. python try except

try except block are used in python to handle errors and exceptions
The code in try block runs when there is no error. If the try block catches the error,
then the except block is executed.

We have value error, memory error, index error etc
'''




try:
    a = int(input("Enter a number: "))

    print(f"\nThe multiplication table of {a} is : ") 
        
    for i in range(1, 11):
        print(f"{a} * {i} = {a*i}")

except TypeError as e:
    print(f"Invalid typ error: {str(e)}")


print("Here are some imp lines of code")
print("End of the code")


#Value error handling

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Number is not an integer")