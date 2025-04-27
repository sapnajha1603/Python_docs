
def decorator_method(func):
    def wrapper():
        print("I am called before the function")
        func()
        print("I am called after the function")
    return wrapper



@decorator_method
def hello():
    print("Hello world this is me")

hello()