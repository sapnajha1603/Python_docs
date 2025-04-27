# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

operator = str(input("Enter the operator: "))

# Print the entered numbers
print(f"The first number is: {num1}")
print(f"The second number is: {num2}")
print(f"The operator is: {operator}")

if operator == "+":
    print(f"The additon of {num1} and {num2} is {num1 + num2}")
if operator == "-":
    print(f"The Subtraction of {num1} and {num2} is {num1 - num2}")
if operator == "*":
    print(f"The Multiplication of {num1} and {num2} is {num1 * num2}")
if operator == "/":
    print(f"The Division of {num1} and {num2} is {num1 / num2}")
if operator == "//":
    print(f"The floor division of {num1} and {num2} is {num1 // num2}")
if operator == "%":
    print(f"The Modulus of {num1} and {num2} is {num1 % num2}")
if operator == "**":
    print(f"The Exponential of {num1} and {num2} is {num1 ** num2}")