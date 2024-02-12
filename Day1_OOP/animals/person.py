class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def introduce(self):
        print(f"My name is {self.name} I am {self.age} and I am {self.height}")

class Superhero:
    def __init__(self, hero_name, hero_identity, hero_power, hero_enemy):
        self.name = hero_name
        self.identity = hero_identity
        self.power = hero_power
        self.enemy = hero_enemy

    def set_new_lair(self, new_lair):
        self.new_lair = new_lair

    def introduce(self):
        print(f"My name is {self.name}, my real name is {self.identity}, my power is {self.power} and my enemy is {self.enemy}")
