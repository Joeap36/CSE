# Items
class Item(object):
    def __init__(self, name):
        self.name = name


class Food(Item):
    def __init__(self, name):
        super(Food, self).__init__(name)


class Weapon(Item):
    def __init__(self, name, durability, bow):
        super(Weapon, self).__init__(name)
        self.name = name
        self.durability = durability
        self.bow = bow


class Armor(Item):
    def __init__(self, name, defense):
        super(Armor, self).__init__(name)
        self.name = name
        self.defense = defense
