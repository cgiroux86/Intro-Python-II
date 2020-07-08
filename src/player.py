# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(object):
    def __init__(self, curr_room, item=[]):
        self.room = curr_room
        self.visited = 0
        self.inventory = item

    def __repr__(self):
        return f'{self.room}, {self.visited}'

    def visit_room(self):
        self.visited += 1

    def update_room(self, room):
        self.room = room

    def add_inv(self, loot):
        self.inventory = self.inventory + [loot]
        print(self.inventory)
