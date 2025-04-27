f = open("tanmay.txt", "r")


l = f.read()


print(l)

k = open("tanmay.txt", "a")

lines = ["This is what i am appending"]
m = k.writelines(lines)


print(m)

f.close()