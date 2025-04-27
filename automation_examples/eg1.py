'''
Write a python script that will first create a folder named examples and inside the folder create 1.c 2.c and so on till 100.c and write 
this is example {i}.c 
2nd task change the file name and the content to 1.cpp and this is example {i}.cpp

1. create  a folder create_folder
2. create c files create_c_files
3. rename the c files to cpp files rename_to_cpp


'''

import os
import shutil


def create_folder(base_dir, folder_name):
    os.chdir(base_dir)
    if os.path.exists(folder_name):
        print(f"{folder_name} already exists, remove it using shutils")
        shutil.rmtree(folder_name)
    os.mkdir(folder_name)

def create_c_files(folder_name, no_of_files):
    os.chdir(folder_name)
    print(f"The current dir now is: {os.getcwd()}")
    for i in range(1, no_of_files):
        file = f"{i}.c"
        with open (file, 'w') as f:
            f.write(f"//Code for {i}.c")

def rename_to_cpp(folder_name):

    print(f"The current dir now is: {os.getcwd()}")

    files = os.listdir()
    print(f"The list of directories are : {files}")

    for file in files:
        if file.endswith('.c'):
            new_file = file.replace('.c', '.cpp')
            os.rename(file, new_file)

def main():
    base_dir = "automation_examples"
    new_dir = "examples"
    no_of_files = 5

    # To create examples folder
    create_folder(base_dir, new_dir)

    # To create c files in examples
    create_c_files(new_dir, no_of_files)

    # To rename c files to cpp
    rename_to_cpp(new_dir)

if __name__ == "__main__":
    main()


