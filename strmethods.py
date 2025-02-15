class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is a {self.age} years old"
    
dog1 = Dog("Buddy",4)
dog2 = Dog("Hydred",7)

print(dog1)
print(dog2)

class Dog:
    species = "Canlline"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def callBy(self):
        print(self.species)
    
dog1 = Dog("Charlie",20)
dog2 = Dog("Bombie",40)
dog3 = Dog("Jumping", 50)
dog1.callBy()

print(dog1.name,dog1.age)
print(dog1.name,dog1.age,dog1.species)