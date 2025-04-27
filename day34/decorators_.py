# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("\nGood Morning")
#     fx(*args, **kwargs)
#     print("Thanks for using this function")
#   return mfx

# @greet
# def hello():
#   print("Hello world")

# @greet
# def add(a, b):
#   print(a+b)
  
# # greet(hello)()

# hello()
# # greet(add)(1, 2)
# add(1, 2)

def decorator_func(func):
    def wrapper():
        print("I am executed before the function call")
        func()
        print("I am executed after the function call")
    return wrapper

@decorator_func
def hello():
    print("Hello world Goodmorning")

hello()
