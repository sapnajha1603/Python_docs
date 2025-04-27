f = open("tani.txt", "w")

lines = ["Hello tani", "How are you", "I hope you are doing good"]

for line in lines:
    f.write(line + '\n')

print(f"Now lets read the content in {f}")


f.close()