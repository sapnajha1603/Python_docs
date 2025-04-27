a = int(input("Enter the first number"))
b = int(input("Enter the Second number"))

def Greater_number(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is smaller than {b}")
    else:
        print(f"{a} is equal to {b}")

Greater_number(a,b)