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
        self.inventory = self.inventory + loot
        print(f"you have picked up {loot}")

    def drop_item(self, i):
        self.inventory = list(map(lambda x: str(x), self.inventory))
        self.inventory = [x for x in self.inventory if x != str(i)]
        print(self.inventory)

    def remove_item(self, item):
        lst = []
        for i in lst:
            print(str(i) == str(item))
            if str(item) in self.inventory and str(item) not in lst:
                lst.append(i)
        self.inventory = lst
        print(self.inventory)
