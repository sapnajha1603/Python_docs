with open('file.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)
    # Read the next 5 bytes
    # dat1 = f.read(5)
    data = f.read()
# print(dat1)
print(data)