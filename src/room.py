# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
import random
items = ['knife', 'sword', 'water', 'gun', 'painkiller',
         'bandage', 'cellphone', 'canned goods', 'treasure chest']


class Room(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.inventory = [Item(x) for x in random.choices(
            items, k=random.choice([1, 2, 3]))] if random.choice([0, 1]) == 0 else None

    def __str__(self):
        return f'name: {self.name}, desc: {self.desc}'
