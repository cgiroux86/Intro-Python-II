from room import Room
from player import Player
import re
import sys


def command_parser():
    print('parser called')
    directions = ['north', 'east', 'south', 'west', 'n', 'e', 's', 'w']
    d = input('Enter a direction: ')
    if d.lower() == 'q':
        print('Thnaks for playing!')
        sys.exit(0)
    while d.lower() not in directions:
        d = input('Please enter a valid direction (North, n, etc: ')
    return d.lower()

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


# # Link rooms together

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


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def find_room(p, d):
    print('room called')
    matched = d[0]
    try:
        if matched == 'n':
            return p.n_to
        elif matched == 'w':
            return p.w_to
        elif matched == 'e':
            return p.e_to
        else:
            return p.s_to

    except AttributeError:
        print('cannot move in this direction')
        r = find_room(p, command_parser())
        return r


def game():
    print('Welcome to the best adventure game in town!\nYou can traverse rooms by entering a direction')
    user = room['outside']
    player = Player('outside')
    while True:
        r = f'{find_room(user, command_parser())}'
        print(r)
        x = re.split(' ', r)[1].lower().replace(',', '')
        x = 'overlook' if x == 'grand' else x
        user = room[x]
        player.visit_room()
        player.update_room(x)
        print(player, user.inventory)

        def decision():
            i = input('Loot found in room! Pick up loot? y/n')
            if i.lower() == 'y' and len(player.inventory) < 6:
                player.add_inv([u for u in user.inventory])
            elif len(player.inventory) > 5:
                ipt = input(
                    'inventory full! Would you like to drop an item? y/n?')
                if ipt.lower() == 'y':
                    dropped = input(
                        f'select which inventory item to drop: {player.inventory}')
                    if str(dropped).lower() in player.inventory:
                        player.drop_item(dropped)
                    else:
                        ipt = input(
                            f'shaky fingers failed you. Please enter a correct item to drop: {player.inventory}')
                        # for val in player.inventory:
                        #     print(str(ip) == str(val), ip, val)
                        while str(ipt) not in player.inventory:
                            print(type(ipt))
                            ipt = input(
                                f'please select a valid item to drop: {player.inventory}')
                        player.drop_item(str(ip))

        decision()


game()
