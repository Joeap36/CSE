# Items
class Item(object):
    def __init__(self, name):
        self.name = name


class Food(Item):
    def __init__(self, name, healing):
        super(Food, self).__init__(name)
        self.healing = healing


class Weapon(Item):
    def __init__(self, name, durability, attack, bow, fire, electric, ice):
        super(Weapon, self).__init__(name)
        self.name = name
        self.durability = durability
        self.attack = attack
        self.bow = bow
        self.fire = fire
        self.electric = electric
        self.ice = ice


class Armor(Item):
    def __init__(self, name, defense):
        super(Armor, self).__init__(name)
        self.name = name
        self.defense = defense
