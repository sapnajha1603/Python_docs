import random

list1 = ["Snake", "Water", "Gun"]

p1 = str(input("Enter your choice:(Snake, Water, Gun): "))
# Get a random value from the list
p2 = random.choice(list1)
print(f"The player 1 choice is : {p1}")
print(f"The Computer choice is : {p2}")

dict1 = {"Snake": 0, "Water": 1, "Gun": 2}

result = [["D", "W", "L"], ["L", "D", "W"], ["W", "L", "D"]]
final = result[dict1[p1]][dict1[p2]]



if final == "D":
    print("OOps the match is drawn")
elif final == "W":
    print("YAyy u won")
else:
    print("You lost the game, try again")

    


