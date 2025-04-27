import os

if not os.path.exists("Understanding_IO"):
    os.mkdir("Understanding_IO")


os.chdir("Understanding_IO")

with open('io_operation.txt', 'w')  as f:
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.write("This is the first statement\n")
    f.close()

with open('io_operation.txt', 'r')  as r:
    list1 = r.readlines()

print(list1)