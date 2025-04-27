'''
The shorthand syntax can be a convinient way to write simple if-else statements
especially when you want to assign a value to a variable based on a cond.
However, its not suitable for more complex situations where you need to execute
multiple statements or perform more complex logic.
In those cases, its best to use the full if-else syntax'''
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"\n The greater value is : {a}") if a > b else print("equal") if a == b else print(f"\nThe greater value is : {b}")



'''
Say we have this if - else statement'''
condition = 10
value_if_true = True
value_if_false = False
if condition:
    result = value_if_true
else:
    result = value_if_false
print(result)

'''
Instead of writing all these lines, we could have simply wrote'''
result = value_if_true if condition else value_if_false
print(result)