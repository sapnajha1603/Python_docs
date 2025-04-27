#single inheritance

class parent():
    def show(self):
        print("This is parent class")

class Child(parent):
    def display(self):
        print("This is the child class")


sapna = Child()
sapna.display()
sapna.show()

#Multiple inheritance

class parent1():
    def show_1(self):
        print("Hey i am parent-1")

class parent2():
    def show_2(self):
        print("Hey i am parent-2")

class child(parent1, parent2):
    def display(self):
        print("Hey i am child")

sapna = child()
sapna.display()
sapna.show_1()
sapna.show_2()

#Multilevel

class grandfather():
    def show_1(self):
        print("Hey i am grandfather")

class father(grandfather):
    def show_2(self):
        print("Hey i am father")
    
class child(father):
    def display(self):
        print("Hey i am child")

sapna = child()
sapna.display()
sapna.show_1()
sapna.show_2()

#Hierarchial

class father():
    def show_1(self):
        print("Hey i am father")

class child2(father):
    def show_2(self):
        print("Hey i am child-2")
    
class child1(father):
    def child_1(self):
        print("Hey i am child-1")

sapna = child1()
sampreeth = child2()
sapna.child_1()
sapna.show_1()
sampreeth.show_2()
sampreeth.show_1()

#Hybrid 
class Parent:
    def parent_feature(self):
        print("Feature from Parent")

class Child1(Parent):
    def child1_feature(self):
        print("Feature from Child1")

class Child2(Parent):
    def child2_feature(self):
        print("Feature from Child2")

class GrandChild(Child1, Child2):  # Multiple + Multilevel
    def grandchild_feature(self):
        print("Feature from GrandChild")

obj = GrandChild()
obj.parent_feature()     # From Parent
obj.child1_feature()     # From Child1
obj.child2_feature()     # From Child2
obj.grandchild_feature() # From GrandChild
