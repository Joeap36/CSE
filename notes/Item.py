# Items
class Item(object):
    def __init__(self, name):
        self.name = name


class Food(Item):
    def __init__(self, name, healing):
        super(Food, self).__init__(name)
        self.healing = healing


class Weapon(Item):
    def __init__(self, name, durability, attack, bow, fire, ice, electric):
        super(Weapon, self).__init__(name)
        self.name = name
        self.durability = durability
        self.attack = attack
        self.bow = bow
        self.fire = fire
        self.ice = ice
        self.electric = electric


class Armor(Item):
    def __init__(self, name, defense):
        super(Armor, self).__init__(name)
        self.name = name
        self.defense = defense


class Character(object):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon


class Enemy(Character):
    def __init__(self, name, weapon, health, itemdrop):
        super(Enemy, self).__init__(name, weapon)
        self.name = name
        self.weapon = weapon
        self.health = health
        self.itemdrop = itemdrop


class Merchant(Character):
    def __init__(self, name, weapon, stock):
        super(Merchant, self).__init__(name, weapon)
        self.name = name
        self.weapon = weapon
        self.stock = stock


master_sword = Weapon("Master Sword", 40, 30, False, False, False, False)
traveler_sword = Weapon("Traveler's Sword", 20, 5, False, False, False, False)
soldier_broadsword = Weapon("Soldier's Broadsword", 25, 14, False, False, False, False)
knight_broadsword = Weapon("Knight's Broadsword", 27, 26, False, False, False, False)
royal_broadsword = Weapon("Royal Broadsword", 36, 36, False, False, False, False)
forest_dweller_sword = Weapon("Forest Dweller's Sword", 27, 22, False, False, False, False)
zora_sword = Weapon("Zora Sword", 27, 15, False, False, False, False)
feathered_edge = Weapon("Feathered Edge", 27, 15, False, False, False, False)
gerudo_scimitar = Weapon("Gerudo Scimitar", 23, 16, False, False, False, False)
moonlight_scimitar = Weapon("Moonlight Scimitar", 32, 25, False, False, False, False)
scimitar_of_the_seven = Weapon("Scimitar of the Seven", 60, 32, False, False, False, False)
eightfold_blade = Weapon("Eightfold Blade", 26, 15, False, False, False, False)
ancient_short_sword = Weapon("Ancient Short Sword", 54, 40, False, False, False, False)
rusty_broadsword = Weapon("Rusty Broadsword", 8, 6, False, False, False, False)
royal_guard_sword = Weapon("Royal Guard's Sword", 14, 48, False, False, False, False)
flameblade = Weapon("Flameblade", 36, 24, False, True, False, False)
frostblade = Weapon("Frostblade", 30, 20, False, False, True, False)
thunderblade = Weapon("Thunderblade", 36, 22, False, False, False, True)
goddess_sword = Weapon("Goddess Sword", 45, 28, False, False, False, False)
boko_club = Weapon("Boko Club", 8, 4, False, False, False, False)
spiked_boko_club = Weapon("Spiked Boko Club", 14, 12, False, False, False, False)
dragonbone_boko_club = Weapon("Dragonbone Boko Club", 18, 24, False, False, False, False)
lizal_boomerang = Weapon("Lizal Boomerang", 17, 14, False, False, False, False)
lizal_forked_boomerang = Weapon("Lizal Forked Boomerang", 25, 24, False, False, False, False)
lizal_triboomerang = Weapon("Lizal Tri-Boomerang", 27, 36, False, False, False, False)
guardian_sword = Weapon("Guardian Sword", 17, 20, False, False, False, False)
guardian_sword_plus = Weapon("Guardian Sword+", 20, 5, False, False, False, False)
guardian_sword_plus_plus = Weapon("Guardian Sword++", 20, 5, False, False, False, False)
