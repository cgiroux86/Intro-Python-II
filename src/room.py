# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
import random
items = ['knife', 'sword', 'water', 'gun', 'painkiller',
         'bandage', 'cellphone', 'canned goods']


class Room(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.item = Item(random.choice(items))

    def __str__(self):
        return f'name: {self.name}, desc: {self.desc}'
