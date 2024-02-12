# class Superhero:
#     def __init__(self, hero_name, hero_identity, hero_power, hero_enemy):
#         self.name = hero_name
#         self.identity = hero_identity
#         self.power = hero_power
#         self.enemy = hero_enemy

# from person import Superhero

class Superhero:
    def __init__(self, hero_name, hero_identity, hero_power, hero_enemy):
        self.name = hero_name
        self.identity = hero_identity
        self.power = hero_power
        self.enemy = hero_enemy
        
    def set_new_lair(self, new_lair):
        self.new_lair = new_lair
    
    def get_lair(self):
        return self.new_lair

    def introduce(self):
        print(f"My name is {self.name}, my real name is {self.identity}, my power is {self.power} and my enemy is {self.enemy}")

batman = Superhero("Batman", "Bruce", "Strong", "The Joker")

batman.set_new_lair("batcave")

print(batman.new_lair)
batman.introduce()

# # print(batman.name, batman.identity, batman.power, batman.enemy)

# print(f"{batman.name}'s real name is {batman.identity}. He is {batman.power} and his arch enemy is {batman.enemy}")

# batman.introduce()

