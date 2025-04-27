'''
The finally code block is also a part of exception handling, when we handle exception using try
and except block, we can include a fianlly block at the end.
The finally block is always executed, so it is generally used for doing the concluding tasks like
closing file resources or closing database connection ot maybe ending the program execution with
a delightful message'''
try:

    list1 = [1,2,3,45,6,5]
    a = int(input("Enter the index of the value you want to know: "))

    print(list1[a])
except:
    print("Some error occured")

finally:
    print(f"List1 has following elements : {list1}")
