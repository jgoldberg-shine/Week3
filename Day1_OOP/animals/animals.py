class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def drink(self):
        print(f"{self.name} is drinking")

class Parrot(Animal):
    def fly(self):
        print (f"{self.name} is flying around")
    
class Fish(Animal):
    def swim(self):
        print (f"{self.name} is having a good swim")