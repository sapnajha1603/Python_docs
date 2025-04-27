import os

if not os.path.exists("Understanding_IO"):
    os.mkdir("Understanding_IO")

statements = ["hii i am sapna\n\t", "hii i am sapna\n"]
os.chdir("Understanding_IO")

with open('io_operation_2.txt', 'a')  as f:
    f.writelines(statements)
    f.close()

with open('io_operation_2.txt', 'r')  as r:
    list1 = r.readlines()

print(list1)