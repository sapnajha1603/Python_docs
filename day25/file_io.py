'''
Python provides several ways to manipulate files.
Opening a File

Before we can perform any operations on a file, we must first open it. 
Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should 
be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

Here's an example of how to open a file for reading:

f = open('sapna.txt', 'r')'''

f = open('sapna.txt', 'r')
text = f.read()
print(text)
f.close()


'''
Modes in file
There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode
 is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to 
the text mode. There is no difference between r and rt or w and wt since text mode is the default. 
The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).
'''


'''
Writing into a file

To write to a file, we first need to open it in write mode.

f = open('myfile.txt', 'w')
We can then use the write() method to write to the file.

f = open('myfile.txt', 'w')
f.write('Hello, world!')
Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.

f = open('myfile.txt', 'a')
f.write('Hello, world!')

'''

f = open('sam.txt', 'w')
f.write('Hello, world!')
f.close()


'''

The 'with' statement
Alternatively, you can use the with statement to automatically close the file after you are done with it.
'''

with open('sam.txt', 'a') as f:
    f.write("Heello from sam\n")
    f.write("Heello from sam\n")
    f.write("Heello from sam\n")
    f.write("Heello from sam\n")
    f.write("Heello from sam\n")
    f.write("Heello from sam\n")

    