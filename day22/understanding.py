'''
if __name__ == "__main__" in Python

The if __name__ == "__main__" idiom is a common pattern used in python scripts to
determine whether the script is being run directly or being imported as a 
module into another script

In python the __name__ variable is a built-in variable that is automatically 
set to the name of the current module.
When a python script is run directly the __name__ variable is set to the
string __main__ . When the script is imported as a module into another script
the __name__ variable is set to the name of the module.

Here's an example of how the if __name__ == __main__ idiom can be used:

'''

import sapna

print(__name__)
sapna.Welcome()

'''
Why is it useful??
This idiom is useful because it allows you to reuse code from a script 
by importing it as a module into another script, without running the code
in the original script.
'''

'''
Is it a necessity??
It's important to note that the if __name__ == "__main__" idiom is not required
to run a python script.
You can still run a script without it by simple calling the function or
running the code you want to execute directly.

However, the if name == main idiom can be useful tool for organising and seperating
code that could be run directly from the code that should be imported as a 
module.

In summary __name__ == "__main__" idiom is a common pattern used in python
scripts to determine whether the script is being run directly or being imported
as a module into another script. It allows you to reuse code from a  script by
importing it as a module into another script, without running the code
in the original script'''



