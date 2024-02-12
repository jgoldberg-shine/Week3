from person import Person

Josh = Person("Josh", 30, "Tall")

print (Josh.age, Josh.height)

class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height
from person import Person


katy = Person("Katy", 31, "short")

katy.introduce()