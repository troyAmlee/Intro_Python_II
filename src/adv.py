from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Troy", "outside")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def initialize_game(player, map):
    game_over = False
    p = player.name
    cr = player.current_room
    key_list = list(map.keys()) 
    val_list = list(map.values()) 
  
    
    

    print(f"\n Welcome to The Dungeon {p} \n \n")
    while(game_over == False):
        print(f"Your location is: {cr} \n")
        print(f'{map[cr].description} \n')
        option = input("What would you like to do? \n1. Move \n2. Quit \n")
        
        if (option.strip() == "1"):
            direction = input("What direction? [n, w, s, e] or [north, west, south, east]: ")
            if (direction.lower() == 'n' or direction.lower() == 'north'):
                if (map[cr].n_to != None):
                    next_room = key_list[val_list.index(map[cr].n_to)]
                    cr = next_room
                else:
                    print(f"You can't go in that direction, {map[cr].directions()}")
            elif (direction.lower() == 'w' or direction.lower() == 'west'):
                if (map[cr].w_to != None):
                    next_room = key_list[val_list.index(map[cr].w_to)]
                    cr = next_room
                else:
                    print(f"You can't go in that direction, {map[cr].directions()}")
            elif (direction.lower() == 'e' or direction.lower() == 'east'):
                if (map[cr].e_to != None):
                    next_room = key_list[val_list.index(map[cr].e_to)]
                    cr = next_room
                else:
                    print(f"You can't go in that direction, {map[cr].directions()}")
            elif (direction.lower() == 's' or direction.lower() == 'south'):
                if (map[cr].s_to != None):
                    next_room = key_list[val_list.index(map[cr].s_to)]
                    cr = next_room
                else:
                    print(f"You can't go in that direction, {map[cr].directions()}")
        elif(option.strip() == '2' or option.strip() == 'quit'):
            break
        else:
            print("\nInvalid option.\n")


initialize_game(player1, room)

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
