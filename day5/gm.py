import time

# print(dir(time))

# current_time = time.strftime('%H:%M:%S')
# # print(f"The time now is: {time.strftime('%H:%M:%S')}")

# print(f"The current time is: {current_time}")

# if current_time >= '00:00:00' and current_time < '12:00:00':
#     print("Good Morning Sir")
# elif current_time >= '12:00:00' and current_time < '17:00:00':
#     print("Good Afternoon sir")
# elif current_time >= '17:00:00' and current_time < '21:00:00':
#     print("Good evening sir")
# else:
#     print("Good Night sir")

'''
String Comparison vs. Time Comparison:

String comparison is lexicographical, meaning it compares each character from left to right. 
This works for most cases but can be error-prone for times not represented in 24-hour format or when leading zeros are present.
For example, 09:00:00 is less than 12:00:00, but 09:00:00 as a string might not be correctly compared if there are issues 
with string formatting or representation.
'''
# Get the current time as a string
current_time_str = time.strftime('%H:%M:%S')
print(f"The current time is: {current_time_str}")

# Convert the current time string to an integer representing the hour
current_hour = int(time.strftime('%H'))

# Determine the appropriate greeting based on the current hour
if 0 <= current_hour < 12:
    print("Good Morning Sir")
elif 12 <= current_hour < 17:
    print("Good Afternoon Sir")
elif 17 <= current_hour < 21:
    print("Good Evening Sir")
else:
    print("Good Night Sir")

