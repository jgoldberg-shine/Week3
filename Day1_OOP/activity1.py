# class Superhero:
#     def __init__(self, hero_name, hero_identity, hero_power, hero_enemy):
#         self.name = hero_name
#         self.identity = hero_identity
#         self.power = hero_power
#         self.enemy = hero_enemy

from person import Superhero
batman = Superhero("Batman", "Bruce", "Strong", "The Joker")

# print(batman.name, batman.identity, batman.power, batman.enemy)

print(f"{batman.name}'s real name is {batman.identity}. He is {batman.power} and his arch enemy is {batman.enemy}")