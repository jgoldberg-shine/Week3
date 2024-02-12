from vehicles import Vehicle, Car, Plane, Train, flyingCar


porsche = Car("Porsche GT3 rs", "small", "200mph", "up to 2")
train = Train("Steam train", "very large", "200mph", "up to 400")
plane = Plane("Boeing 747", "large", "650mph", "up to 300")
special = flyingCar("", "", "", "")

porsche.introduce() 
porsche.road()

train.introduce()
train.track()

plane.introduce()
plane.fly()

special.both()