def my_generator():
    for i in range(5000):
        yield i
    

gen = my_generator()
for i in range(5000):
    print(next(gen))