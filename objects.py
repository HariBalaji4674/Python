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
