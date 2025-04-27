# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret
#  code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains encode than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


input1 = input(str("\nPlease enter a string: "))

rev = ""
left = "msd"
right = "mtr"
encode = ""
decode = ""
"""
Encoding"""
if len(input1) >= 3:

    encode = input1[1:] + input1[0]
    encode = left + encode + right


else:
    encode = input1[::-1]


print(f"The encoded string for {input1} is {encode}")

"""
Decoding"""

if len(encode) < 3:
    decode = encode[::-1]

else:
    decode = encode[3:-3]
    decode = decode[-1] + decode[0:-1]


print(f"The decoded string for {encode} is {decode}")







