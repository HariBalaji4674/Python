class objects:
    attr1 = "mamal"
    attr2 = "dog"
    def one(self,a,b):
        self.a = a
        self.b = b
        return a**b
    def two(self):
        print(self.attr1,self.attr2)

obj1 = objects()

val = obj1.one(2,3)
obj1.two()
print(val)


class Main1:
    attr1 = "Peddireddy1"
    attr2 = "Peddireddy2"
    def __init__(self,name):
        self.name = name
    def Method1(self):
        return f"My name is {self.name} "
    
object1 = Main1("Peddireddy3")
print(object1.attr1)
print(object1.attr2)
print(object1.Method1())


class MyNumber:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        print(self.name)

obj1 = MyNumber("peddireddy")
obj1.print_name()

# self is a constructor in classes
# self is pointer to current object
# 

class SelfObject:
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2

obj = SelfObject("Hari","Vardhan")
print(obj.name1)
print(obj.name2)

class Check():
    def __init__(self):
        print("Address of Self = ", id(self))
    
obj = Check()
print("Adderesss of Object ", id(obj))

# Creating Class with attributes and Methods

