a = int(input("Enter a number: "))

if a > 0:
    print(f"{a} is a positive number")
elif a == 0:
    print(f"{a} is zero")
else:
    print(f"{a} is a negative number")

'''
Never use a module name as your file name, like dont save your python file as if.py because instead of searching in if.py in python, 
it will try to find it in your code if.py file
'''