class Vehicle:
    def __init__(self, vehicle_type, vehicle_size, vehicle_maxspeed, vehicle_passengers):
        self.type = vehicle_type
        self.size = vehicle_size
        self.maxspeed = vehicle_maxspeed
        self.passengers = vehicle_passengers
        
    def introduce(self):
        print(f"A {self.type}, is a {self.size} vehicle with a max speed of {self.maxspeed} and can carry up to {self.passengers} passengers")

class Car(Vehicle):
    def road(self):
        print(f"A {self.type} drives on the road")

class Plane(Vehicle):
    def fly(self):
        print(f"A {self.type} can fly")

class Train(Vehicle):
    def track(self):
        print(f"A {self.type} travels on a track")

class flyingCar(Car, Plane):
    def both(self):
        print(f"A {self.type} can go a road and in the air")

