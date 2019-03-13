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


class Character(object):
    def __init__(self, name, weapon, health, armor):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.armor = armor


master_sword = Weapon("Master Sword", 20, 5, False, False, False, False)
traveler_sword = Weapon("Traveler's Sword", 20, 5, False, False, False, False)
soldier_broadsword = Weapon("Soldier's Broadsword", 25, 14, False, False, False, False)
knight_broadsword = Weapon("Knight's Broadsword", 27, 26, False, False, False, False)
royal_broadsword = Weapon("Royal Broadsword", 36, 36, False, False, False, False)
forest_dweller_sword = Weapon("Forest Dweller's Sword", 27, 22, False, False, False, False)
zora_sword = Weapon("Zora Sword", 27, 15, False, False, False, False)
feathered_edge = Weapon("Feathered Edge", 27, 15, False, False, False, False)