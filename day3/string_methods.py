'''
Strings are immutable 
So when i say .upper() on a string object that means python creates
a new string, which is upper(a), a is not really changed to upper
'''
a = "Sapna"
print(a)
print(a.upper())
a = a.upper()
print(a)
print(a.lower())

b = "!!!!Sapna is a new joinee!!!!!"
print(b.strip("!"))

c = "Sapna is too angry now"
print(c.replace("angry","happy"))

'''
Say now i want to use split(), now say we have 3 names, we want to split it based
on " " and convert it into a list
'''
d = "Sapna Tanmay Tanisha"
print(d.split(" "))
d1_list = d.split(" ")
print(d1_list)

'''
When we use capitalize() then the first letter will be capitalized. So
first job that capitalize does is to make the first character uppercase, and make
all the other characters lowercase
'''
e = "tanmay is mY besT friend"
print(e.capitalize())

f = "Tanisha and Tanmay are Truelly soo cute"
print(f.count("T"))

g = "Lets see if this statement ends with $$$$$$$$"
print(g.endswith("!"))
print(g.endswith("$"))

h = "I want to find index of sapna in the string"
print(h.find("sapna"))
print(h.find("tanmi")) #this will just give true or false
#If we are sure that the index of the string will be present then we can use index()
print(h.index("sapna"))
# print(h.index("tanmi")) #this will cause an error

'''
isalnum() returns true if the string only consists of alphabets or numericals
A-Z, a-z, 0-9
Even if you have spaces in your string, it will return false
'''
i = "Helloworld13467768"
print(i.isalnum())
j = "HJCSDKCWEASOD 817239I"
print(j.isalnum())


k = "helloworld"
print(k.isalpha())

l = "helloworld"
print(l.islower())
print(l.isupper())

'''
Try for 
isprintable
isspace
istitle is used to check if first letter of each word is capitalized or not
startswith
swapcase converts lowercase to uppercase and uppercase to lowercase
title capitalizes each letter of the word within the string
'''

str1 = ""
str1 = str1 + "abc"
# str.add("abc") These 2 methods are not gonna work because strings are immutable so you cant add or append you will have to create  a new string and add your string in it
# str.append("abc")
print(str1)

new = "hello i am sapna"
print(new.title())
print(new)

