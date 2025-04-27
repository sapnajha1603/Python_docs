import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 100):
    dir_name = f"data/Day{i+1}"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
