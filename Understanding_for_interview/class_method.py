class Myclass:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
    @classmethod
    def final_count(cls):
        print(f"The final count is : {cls.count}")

obj1 = Myclass.increment()
obj2 = Myclass.increment()
obj3 = Myclass.increment()
obj4 = Myclass.increment()
obj4 = Myclass.increment()
obj5 = Myclass.increment()
obj6 = Myclass.increment()
obj7 = Myclass.increment()
obj8 = Myclass.final_count()

