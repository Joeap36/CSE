# Items
class Item(object):
    def __init__(self, name):
        self.name = name


class Food(Item):
    def __init__(self, name, healing):
        super(Food, self).__init__(name)
        self.healing = healing


class Weapon(Item):
    def __init__(self, name, durability, attack):
        super(Weapon, self).__init__(name)
        self.name = name
        self.durability = durability
        self.attack = attack


class Bow(Weapon):
    def __init__(self, name, durability, attack, shots):
        super(Bow, self).__init__(name, durability, attack)
        self.name = name
        self.durability = durability
        self.attack = attack
        self.shots = shots


class ElecWeapon(Weapon):
    def __init__(self, name, durability, attack):
        super(ElecWeapon, self).__init__(name, durability, attack)
        self.name = name
        self.durability = durability
        self.attack = attack


class IceWeapon(Weapon):
    def __init__(self, name, durability, attack):
        super(IceWeapon, self).__init__(name, durability, attack)
        self.name = name
        self.durability = durability
        self.attack = attack


class FireWeapon(Weapon):
    def __init__(self, name, durability, attack):
        super(FireWeapon, self).__init__(name, durability, attack)
        self.name = name
        self.durability = durability
        self.attack = attack


class Armor(Item):
    def __init__(self, name, defense, slot):
        super(Armor, self).__init__(name)
        self.name = name
        self.defense = defense
        self.slot = slot


class FireArmor(Armor):
    def __init__(self, name, defense, slot):
        super(FireArmor, self).__init__(name, defense)
        self.name = name
        self.defense = defense
        self.slot = slot


class IceArmor(Armor):
    def __init__(self, name, defense, slot):
        super(IceArmor, self).__init__(name, defense)
        self.name = name
        self.defense = defense
        self.slot = slot


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


# Weapons
master_sword = Weapon("Master Sword", 40, 30)
traveler_sword = Weapon("Traveler's Sword", 20, 5)
soldier_broadsword = Weapon("Soldier's Broadsword", 25, 14)
knight_broadsword = Weapon("Knight's Broadsword", 27, 26)
royal_broadsword = Weapon("Royal Broadsword", 36, 36)
forest_dweller_sword = Weapon("Forest Dweller's Sword", 27, 22)
zora_sword = Weapon("Zora Sword", 27, 15)
feathered_edge = Weapon("Feathered Edge", 27, 15)
gerudo_scimitar = Weapon("Gerudo Scimitar", 23, 16)
moonlight_scimitar = Weapon("Moonlight Scimitar", 32, 25)
scimitar_of_the_seven = Weapon("Scimitar of the Seven", 60, 32)
eightfold_blade = Weapon("Eightfold Blade", 26, 15)
ancient_short_sword = Weapon("Ancient Short Sword", 54, 40)
rusty_broadsword = Weapon("Rusty Broadsword", 8, 6)
royal_guard_sword = Weapon("Royal Guard's Sword", 14, 48)
goddess_sword = Weapon("Goddess Sword", 45, 28)
boko_club = Weapon("Boko Club", 8, 4)
spiked_boko_club = Weapon("Spiked Boko Club", 14, 12)
dragonbone_boko_club = Weapon("Dragonbone Boko Club", 18, 24)
lizal_boomerang = Weapon("Lizal Boomerang", 17, 14)
lizal_forked_boomerang = Weapon("Lizal Forked Boomerang", 25, 24)
lizal_triboomerang = Weapon("Lizal Tri-Boomerang", 27, 36)
guardian_sword = Weapon("Guardian Sword", 17, 20)
guardian_sword_plus = Weapon("Guardian Sword+", 20, 5)
guardian_sword_plus_plus = Weapon("Guardian Sword++", 20, 5)
lynel_sword = Weapon("Lynel Sword", 26, 24)
mighty_lynel_sword = Weapon("Mighty Lynel Sword", 32, 36)
savage_lynel_sword = Weapon("Savage Lynel Sword", 41, 58)
vicious_sickle = Weapon("Vicious Sickle", 14, 16)
demon_carver = Weapon("Demon Carver", 25, 40)

# Electric Weapons
thunderblade = ElecWeapon("Thunderblade", 36, 22)
lightning_rod = ElecWeapon("Lightning Rod", 14, 5)
thunderstorm_rod = ElecWeapon("Thunderstorm Rod", 32, 10)

# Ice Weapons
frostblade = IceWeapon("Frostblade", 30, 20)
ice_rod = Weapon("Ice Rod", 14, 5)
blizzard_rod = Weapon("Blizzard Rod", 32, 10)

# Fire Weapons
flameblade = FireWeapon("Flameblade", 36, 24)
fire_rod = FireWeapon("Fire Rod", 14, 5)
meteor_rod = FireWeapon("Meteor Rod", 32, 10)
