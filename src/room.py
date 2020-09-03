# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, itemlist = [], enemylist = []):
        self.name = name.lower()
        self.description = description
        self.itemlist = itemlist
        self.enemylist = enemylist
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name}: {self.description}"

    def directions(self):
        direction = []
        if (self.n_to != None):
            direction.append("north")
        if (self.s_to != None):
            direction.append("south")
        if (self.e_to != None):
            direction.append("east")
        if (self.w_to != None):
            direction.append("west")
        return f"\nDirections available: {direction}\n" 

        