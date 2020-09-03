# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, satchel, health, base_damage):
        self.name = name
        self.current_room = current_room
        self.satchel = satchel # list of items the player carries
        self.health = health
        self.base_damage = base_damage
    def __str__(self):
        return f"{self.name} your location: {self.current_room}"
    def move(self, location):
        self.current_room = location
    def attack(self, damage):
        total_damage = damage + self.base_damage
        return total_damage
    def pickup(self, item):
        self.satchel.append(item)
    def drop(self, item, room):
        self.satchel.pop()


class Enemy(Player):
    def __init__(self, name, current_room, satchel, health, base_damage):
        super().__init__(name, current_room, satchel, health, base_damage)
    
