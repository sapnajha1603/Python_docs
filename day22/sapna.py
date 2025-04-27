def Welcome():
    print("Hello and welcome from Sapna")

print(__name__)

'''
Say you have a file named sapna.py. Now you want to use this file in sam.py and call function Welcome, so you just import sapna and
call sapna.Welcome()

Now this will result in Hello and welcome from Sapna printed twice because 
after import sapna, the code will run this file and here it sees Welcome(), now the code will execute it and then again i am calling 
sapna.Welcome() so again it will print Hello and welcome from Sapna

Now to avoid this issue we use if __name__ == "__main__" 
This if condition will check whether name is main or not

Now to understand __name__ this is a good def
In Python, the special built-in variable __name__ is set to "__main__" when a script is run directly.
This allows the script to distinguish between when it is run directly and when it is imported as a module in another script.

So when i run sapna.py alone, it will print __name__ value as __main__
But when i import sapna into sam.py, then when __name__ is printed, it will print __sapna__ because the import is importing
module sapna and thus the name is saved as sapna


So to avoid the two times printing or you can say you have some scripts where in the script you are calling functions multiple times, and
then importin it as well into other scripts, then __name == "main" can come to your rescue, since it will only execute functions if name is 
main'''

# Welcome()



if __name__ == "__main__":
    Welcome()
