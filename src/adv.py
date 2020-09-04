from room import Room
from player import Player
from item import Item
from item import Weapon
from item import Armor
from item import Potion

# Declare all the rooms


items = {
    'rustysword': Weapon("Rusty Sword", "A worn and battle tested sword, seems dull", 100),
    'silversword': Weapon("Silver Sword", "Made of 75 percent silver and 25 percent titanium alloy, the engraving reads 'Excalibur'", 750),
    'shield': Armor("Shield", "A trusty shield", 0.90),
    'lowpotion': Potion("Low Potion", "It has a translucent glow", 100)
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['rustysword'], items['shield'], items['lowpotion']]),

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
player1 = Player("Troy", "outside", [], 1000, 25) # name, current_room, satchel, health, base_damage
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def print_inventory():
    curr_inv = []

    keys_list = list(items.keys()) 
    vals_list = list(items.values())

    for i,j in enumerate(vals_list):
        for k in player1.satchel:
            if (j == k):
                curr_inv.append(keys_list[i])
    
    return curr_inv

def room_items():
    room_inv = []

    keys_list = list(items.keys()) 
    vals_list = list(items.values())

    for k in room[player1.current_room].itemlist:
        for i,j in enumerate(vals_list):
            if (j == k):
                room_inv.append(keys_list[i])
    
    return room_inv

def pickup_item(option, current_room):
    

    # arr = []

    # keys_list = list(items.keys()) 
    # vals_list = list(items.values())

    # for j,l in enumerate(vals_list):
    #     for i,k in enumerate(room[current_room].itemlist):
    #         if(l == room[current_room].itemlist[i]):
    #             arr.append(keys_list[j])


    item_list = room_items() # ['rustysword', 'shield', 'lowpotion']


    item_index = item_list.index(option) # 'rustysword == player option selected

    item_selected = room[current_room].itemlist.pop(item_index) # 'outside' == current_room
    item_list.pop(item_index)
    

    player1.satchel.append(item_selected)

    print(f"\n You now have {[i.name for i in player1.satchel]}\n")



def drop_item(option, current_room):
    inventory = print_inventory()

    # keys_list = list(items.keys()) 
    # vals_list = list(items.values())

    for i, k in enumerate(inventory):
        if (option == k):
            dropped = player1.satchel.pop(inventory.index(k))
    room[current_room].itemlist.append(dropped)

    print(room[current_room].itemlist)




def battle_sequence(theplayer, theenemy):
    pass

def initialize_game(player, map, itemlist):
    game_over = False
    p = player.name
    cr = player.current_room
    key_list = list(map.keys()) 
    val_list = list(map.values()) 

    print(f"\n Welcome to The Dungeon {p} \n \n")
    item_list = list(items.keys())
    while(game_over == False):
        print(f"Your location is: {cr} \n")
        print(f'{map[cr].description} \n')
        option = input("What would you like to do? \n1. Move \n2. Quit \n3. Search\n4. Drop Item\n5. Inventory\n")

        
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
        elif(option.strip() == '2' or option.strip().lower() == 'quit'):
            break
        elif(option.strip() == '3' or option.strip().lower() == 'search'):
            il = room_items()
            print(f"You find: {il}")
            print("You think about what you need to take: \n")
            for (j, k) in enumerate(il):
                print(f"{j+1}: {k}")
            selection = input("You choose an item: ")
            for i, l in enumerate(il):
                if (selection == il[i]):
                    pickup_item(selection, cr)
                    break
                    # item_list.pop(i)

        elif(option.strip() == '4' or option.strip().lower() == 'dropitem' or option.strip().lower() == 'drop'):
            inv = print_inventory()
            print(inv)
            selection = input("You choose an item: ")
            if (len(inv) == 0):
                    print("\n Your inventory is empty. \n")
            else:
                for i in inv:
                    if (selection == i):
                        drop_item(selection, cr)
                    else:
                        print("Invalid selection...")
        elif(option.strip() == '5' or option.strip().lower() == 'inventory'):
            print(f"\n Current Inventory:  {print_inventory()} \n")

        else:
            print("\nInvalid option.\n")


initialize_game(player1, room, items)

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
