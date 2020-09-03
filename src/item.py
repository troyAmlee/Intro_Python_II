class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}: {self.description}"

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage # multiplies base damage by a percentage


class Armor(Item):
    def __init__(self, name, description, protection):
        super().__init__(name, description)
        self.protection = protection # takes damage off by a percentage i.e (enemy_damage*0.75)

class Potion(Item):
    def __init__(self, name, description, healing):
        super().__init__(name, description)
        self.healing = healing # an integer that will heal HP slightly