import time

current_time = time.strftime('%H:%M:%S')
print(current_time)


current_hour = int(time.strftime('%H'))
print(current_hour)

if current_hour < 12 and current_hour > 0:
    print("Good Morning")
elif current_hour > 12 and current_hour < 17:
    print("Good afternoon")
elif current_hour > 17 and current_hour < 20:
    print("Good evening")
else:
    print("Good night")