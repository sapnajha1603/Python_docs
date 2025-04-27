def calculator(num1, num2, operator):
    if operator == "+":
        print(f"The addition of num1 and num2 is: {num1+num2}")
    elif operator == "-":
        print(f"The substraction of num1 and num2 is : {num1-num2}")
    elif operator == "*":
        print(f"The Multiplication of num1 and num2 is : {num1*num2}")
    elif operator == "/":
        print(f"The Division of num1 and num2 is : {num1/num2}")
    elif operator == "**":
        print(f"num1 power num2 is : {num1**num2}")
    elif operator == "//":
        print(f"The floor division of num1 and num2 is : {num1//num2}")
    else:
        print(f"Invalid operator")


inp1 = float(input("Enter the first number\n"))
inp2 = float(input("Enter the second number\n"))
operator = str(input("Enter the operator\n"))
calculator(inp1, inp2, operator)
