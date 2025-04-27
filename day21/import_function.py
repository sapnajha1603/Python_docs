'''
Importing in python is the process of loading code from python module
into the current script.
This allows you to use the functions and variables defined in the module in 
yout current script, as well as any additional modules that the imported 
module may depend on.

To import a module in python, you use the import statement followed by the name of
the module.
For eg, to import math module, which contains a variety of mathemantical
functions, you would use the following statement

Once module is imported, you can use any of the functions and variables
defined in the module by using the dot notation.
For eg, to use the sqrt from the math module, you would write'''


import math
result = math.sqrt(9)
print(result)


'''
from keyword

You can also use import specific functions ot variables from the module
using the from keyword. For eg, to import only the sqrt funtion from the
math module, you would write'''

from math import sqrt
result = sqrt(9)
print(result)


'''
You can also import multiple functions or variables at once by seperating
them with a comma'''

from math import sqrt, pi
result = sqrt(9)

print(result)

print(pi)


'''
Importing everything

It's also possible to import all functions and variables from a module
using the * wildcard.
However, this is generally not recommended as it as can lead to confusion
and make it harder to understand where specific functions and variables
are coming from'''
from math import *
result = sqrt(9)

print(result)

print(pi)

"""
The "as" keyword
Python allows you to rename imported modules using the as keyword.
This can be useful if you want to use a shorter or more desciptive
name for a module, or if you want to avoid naming conflicts with other modules
or variables in your code"""


import math as m
result = m.sqrt(9)
print(result)


'''
The dir function
Finally python has a built-in function called dir that you can use to view names
of all the functions and variables defined in a module.
This can be helpful for exploring and understanding the contents of a new module


This will output a list of all the names defined in the math module, including
functions like sqrt and pi, as well as other variables and constants'''


import math
print(dir(math))


'''
In summary, the import statement in python allows you to access the functions and 
variables defined in a module from within your current script.
You can import the entire module, specific functions or variables,
or use the * wildcard to import everything
You can also use the keyword to rename a module, and the dir function to view 
the contents of module

'''



