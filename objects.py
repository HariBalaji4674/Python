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