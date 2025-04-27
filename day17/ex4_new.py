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
split_ip = input1.split()
print(input1)
encode_list = []
decode_list = []
rev = ""
left = "msd"
right = "mtr"
encode = ""
decode = ""
"""
Encoding"""

for ip in split_ip:
    if len(ip) >= 3:
        encode = ip[1:] + ip[0]
        encode = left + encode + right
        encode_list.append(encode)
        print(encode_list)


    else:
        encode = input1[::-1]
        encode_list.append(encode)




"""
Decoding"""

for ip in encode_list:
    if len(ip) >= 3:
        decode = ip[3:-3]
        decode = ip[-1] + ip[0:-1]
        decode_list.append(decode)


    else:
        decode = ip[::-1]
        decode_list.append(decode)

print(f"The encoded string for {input1} is {str(encode_list)}")


print(f"The decoded string for {encode} is {str(decode_list)}")



# import random
# import string
# a=random.choices(string.ascii_letters, k=3)
# print(a)



