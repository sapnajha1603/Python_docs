'''
Python allows the else keyword to be used with the for loop and while looop too.
The else block appears after the body of the loop.
The statements in the else block will be executed after all iterations are
completed.
The program exits the loop only after the else block is executed'''


# for i in range(5):
#     print(i)
# else:
#     print("We are out of the loop")


#Now lets try a break cond
'''
Here no else was executed because else thinks that the entire for loop was executed successfully
In simple words its like , here for-else is like a loop, now when you put break, the entire loop is breaked
That means even the else loop gets breaked'''
for i in range(5):
    if (i == 3):
        break
    print(i)
else:
    print("We are out of the loop")

#Using while and else
i = 0
while (i < 7):
    print(i)
    i += 1
else:
    print("We are out of the loop")

# while else and break

i = 0
while (i < 7):
    if (i == 5):
        break
    print(i)
    i += 1
else:
    print("We are out of the loop")