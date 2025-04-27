# This is called breaking out of the loop
for i in range(1, 12):
    if (i == 11):
        break
    print(f"5 * {i} = {5 * i }")

print("Now let's try continue statement")

for i in range(1, 12):
    if (i == 8):
        continue
    print(f"5 * {i} = {5 * i }")

