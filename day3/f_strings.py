'''
It is a new string formatting mechanism introduced by the PEP 498
It is also know as literal string interpolation or more commonly named
as F-Strings(f character preceding the string literal()), the primary focus of this
of this mechanism is to make the interpolation easier.

When we prefix the string with letter "f", the string becomes the f-string itself.
The f-string can be formatted in much same as str.format() method. The
f-string offers a convenient way to embed python expression inside string literals 
for formatting.
'''


name = "Sapna Jha"
country = "India"
dob = "16-03-2001"
print(f"Hii My name is {name} and i am from {country} and i was born on {dob}")


'''
Say u want to print the string with the brackets instead of value, now when you give {name} it takes the name but say u want to print 
it like {name} then you can do this
'''
print(f"Hii My name is {{name}} and i am from {{country}} and i was born on {{dob}}")

print("Hii My name is {name} and i am from {country} and i was born on {dob}")