class main:
    def bark(self,a):
        self.a = a
        return a**2

d = main()
e = d.bark(10)
print(e)

# Methods

def one(a):
    return a
def two(b):
    return b**2
def three(c):
    return c**1

d = one(10)*two(4)*three(7)

print(d)

# self is an instance of the class should be passed in method mandatorily

class selfClass:
    def main1(hari,a,b):
        hari.a = a
        hari.b = b
        print(a+a+b)


selfClass().main1(20,30)
# d.main1(20,30)
# print(d)

# __init__ method is a constructor in python

class initMethod:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def values(self):
        return self.a**self.b

# initMethod() # TypeError: initMethod.__init__() missing 2 required positional arguments: 'a' and 'b'
# initMethod(20,30) # TypeError: __init__() should return None, not 'int'
c = initMethod(20,30)
d = c.values()
print(d)

class car:
    def __init__(self,model,color):
        self.model = model
        self.color = color
    def show(self):
        print(f"model of car {self.model}")
        print(f"color of car {self.color}")

audi = car("audi","blue")
ferari = car("ferari","red")

audi.show()
ferari.show()

hyndai = car("hyndai","yellow")
hyndai.show()

class Dog:
    def mainMethod(self):
        print(self.name)

cl1 = Dog()
cl1.mainMethod("peddireddy")