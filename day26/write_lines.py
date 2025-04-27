f = open("tanmay.txt", "w")

lines = ["Hello Tanmay\n", "How are you\n", "You are a very good boy\n"]

f.writelines(lines)


f.close()


k = open("tanmay.txt", "r")

lines = k.readlines()

print(lines)
f.close()


