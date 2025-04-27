a = int(input("Enter a number"))


match a:
    case 1: 
        print("a is 1")
    case 2:
        print("a is 2")
    case _:
        print("a is neither 1 nor 2")