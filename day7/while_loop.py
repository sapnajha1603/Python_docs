'''
You can use while and else together, when the while and else are used together, if the while cond is failed then it executes the else 
condition

There is no do-while in python
syntax for do while just fot understanding
do
{
#loop body
}while(condition)
It will run the while loop once and then check the condition

How to emulate do while loop in python???
'''

# i = 0
# while( i <= 10):
#     print(i)
#     i += 1
# else:
#     print("I am outside while")

# To emulate a do while loop in python we can do this

j = 0
while True:
    print(j)
    if (j == 10):
        print("Coming out of the loop")
        break
    j += 1