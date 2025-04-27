def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    

print(f"The factorial is : {factorial(5)}")


def fibo(n):
    '''
    For fibonacci series
    remember 
    f(0) = 0
    f(1) = 1
    say u have to find fibonacci value of 7
    then 
    f(0) = 0
    f(1) = 1
    f(2) = f(0) + f(1) = 0+1 = 1
    f(3) = f(2) + f(1) = 1 + 1 = 2
    f(4) = 2 + 1 = 3
    f(5) = 3 + 2 = 5
    f(6) = 5 + 3 = 8
    f(7) = 8 + 5 = 13
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(f"The fibonacci value is : {fibo(8)}")

# print(fibo.__doc__)