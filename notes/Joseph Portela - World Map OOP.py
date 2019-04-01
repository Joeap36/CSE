class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, worp=None, description=None, items=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.worp = worp
        self.description = description
        self.items = items


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
        self.durability = durability
        self.attack = attack


class Bow(Weapon):
    def __init__(self, name, durability, attack, shots):
        super(Bow, self).__init__(name, durability, attack)
        self.durability = durability
        self.attack = attack
        self.shots = shots


class ElecWeapon(Weapon):
    def __init__(self, name, durability, attack):
        super(ElecWeapon, self).__init__(name, durability, attack)
        self.durability = durability
        self.attack = attack


class IceWeapon(Weapon):
    def __init__(self, name, durability, attack):
        super(IceWeapon, self).__init__(name, durability, attack)
        self.durability = durability
        self.attack = attack


class FireWeapon(Weapon):
    def __init__(self, name, durability, attack):
        super(FireWeapon, self).__init__(name, durability, attack)
        self.durability = durability
        self.attack = attack


class Armor(Item):
    def __init__(self, name, defense, slot):
        super(Armor, self).__init__(name)
        self.defense = defense
        self.slot = slot


class FireArmor(Armor):
    def __init__(self, name, defense, slot):
        super(FireArmor, self).__init__(name, defense, slot)


class HeatArmor(Armor):
    def __init__(self, name, defense, slot):
        super(HeatArmor, self).__init__(name, defense, slot)


class ColdArmor(Armor):
    def __init__(self, name, defense, slot):
        super(ColdArmor, self).__init__(name, defense, slot)


class ElecArmor(Armor):
    def __init__(self, name, defense, slot):
        super(ElecArmor, self).__init__(name, defense, slot)


class AttackArmor(Armor):
    def __init__(self, name, defense, slot):
        super(AttackArmor, self).__init__(name, defense, slot)


class SneakArmor(Armor):
    def __init__(self, name, defense, slot):
        super(SneakArmor, self).__init__(name, defense, slot)


class Character(object):
    def __init__(self, name):
        self.name = name


class Enemy(Character):
    def __init__(self, name, damage, health):
        super(Enemy, self).__init__(name)
        self.damage = damage
        self.health = health


class Merchant(Character):
    def __init__(self, name, stock):
        super(Merchant, self).__init__(name)
        self.stock = stock


# Normal items
arrow = "arrow"

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
woodcutter_axe = Weapon("Woodcutter's Axe", 47, 3)
double_axe = Weapon("Double Axe", 52, 18)
iron_sledgehammer = Weapon("Iron Sledgehammer", 40, 12)
traveler_claymore = Weapon("Traveler's Claymore", 20, 10)
soldier_claymore = Weapon("Soldier's Claymore", 25, 20)
knight_claymore = Weapon("Knight's Claymore", 30, 38)
royal_claymore = Weapon("Royal Claymore", 40, 52)
silver_longsword = Weapon("Silver Longsword", 30, 22)
cobble_crusher = Weapon("Cobble Crusher", 30, 15)
stone_smasher = Weapon("Cobble Crusher", 40, 42)
boulder_breaker = Weapon("Boulder Breaker", 60, 60)
golden_claymore = Weapon("Golden Claymore", 30, 28)
eightfold_longblade = Weapon("Eightfold Longblade", 25, 32)
edge_of_duality = Weapon("Edge of Duality", 35, 50)
ancient_bladesaw = Weapon("Ancient Bladesaw", 50, 55)
rusty_claymore = Weapon("Rusty Claymore", 10, 12)
royal_guard_claymore = Weapon("Royal Guard's Claymore", 15, 72)

# Electric Weapons
thunderblade = ElecWeapon("Thunderblade", 36, 22)
lightning_rod = ElecWeapon("Lightning Rod", 14, 5)
thunderstorm_rod = ElecWeapon("Thunderstorm Rod", 32, 10)

# Ice Weapons
frostblade = IceWeapon("Frostblade", 30, 20)
ice_rod = IceWeapon("Ice Rod", 14, 5)
blizzard_rod = IceWeapon("Blizzard Rod", 32, 10)

# Fire Weapons
flameblade = FireWeapon("Flameblade", 36, 24)
fire_rod = FireWeapon("Fire Rod", 14, 5)
meteor_rod = FireWeapon("Meteor Rod", 32, 10)

# Bows
wooden_bow = Bow("Wooden Bow", 20, 4, 1)

# Armor
amber_earrings = Armor("Amber Earrings", 4, 1)

# Cold Armor
snowquill_headress = ColdArmor("Snowquill Headdress", 3, 1)

# Heat Armor
sapphire_circlet = HeatArmor("Sapphire Circlet", 3, 1)

# Fire Armor
flamebreaker_helm = FireArmor("Flamebreaker Helm", 3, 1)

# Attack Armor
fierce_deity_mask = AttackArmor("Fierce Deity Mask", 3, 1)

# Stealthy Armor
stealth_mask = SneakArmor("Stealth Mask", 2, 1)

# Food
apple = Food("Apple", 1)

# Enemy
red_bokoblin = Enemy("Red Bokoblin", 1, 13)

# Merchant
beetle = Merchant("Beetle", [boko_club, wooden_bow])


class Player(object):
    def __init__(self, starting_location, inventory):
        self.current_location = starting_location
        self.inventory = inventory

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location:  The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction.

        :param direction: The direction that you want to move to
        :return: The Room Object if it exists, or None if it does not
        """
        return getattr(self.current_location, direction)


vworp = Room("Vworp", None, None, None, None, None, "Vworp")
white = Room("The White Room", None, None, None, None, None,
             "The room is almost blindingly white, there"
             "are four passages, each on one side of the"
             "room. Violet is to the south, scarlet is to"
             "the east, yellow is to the north, and"
             "turquoise is to the west.",
             [traveler_sword]
             )
yellow = Room("The Yellow Room", None, None, white, None, None,
              "The room is completely yellow. Four exits, one"
              "on each wall, leave the room. Orange yellow is"
              "to the north, red is to the east, white is to"
              "the south, and yellow green is to the west."
              )
scarlet = Room("The Scarlet Room", None, None, None, white, None,
               "The room is completely scarlet. Four exits,"
               "one on each wall, leave the room. red is to"
               "the north, crimson is to the east, purple is"
               "to the south, and white is to the west."
               )
violet = Room("The Violet Room", white, None, None, None, None,
              "The room is completely violet. Four exits, one"
              "on each wall, leave the room. White is to the"
              "north, purple is to the east, blue violet is to"
              "the south, and cyan blue is to the west."
              )
turquoise = Room("The Turquoise Room", None, white, None, None, None,
                 "The room is completely turquoise. Four exits, one"
                 "on each wall, leave the room. Yellow green is to"
                 "the north, white is to the east, cyan blue is to"
                 "the south, and blueish green is to the west."
                 )
red = Room("The Red Room", None, None, scarlet, yellow, None,
           "The room is completely red. Four exits, one"
           "on each wall, leave the room. Orange is to the"
           "north, scarlet red is to the east, scarlet is"
           "to the south, and yellow is to the west."
           )
purple = Room("The Purple Room", scarlet, None, None, violet, None,
              "The room is completely purple. Four exits, one"
              "on each wall, leave the room. Scarlet is to the"
              "north, magenta is to the east, purple violet is"
              "to the south, and violet is to the west."
              )
cyan_blue = Room("The Cyan Blue Room", turquoise, violet, None, None, None,
                 "The room is completely cyan blue. Four exits,"
                 "one on each wall, leave the room. Turquoise"
                 "is to the north, violet is to the east, blue"
                 "is to the south, and greenish cyan is to the"
                 "west."
                 )
yellow_green = Room("The Yellow Green Room", None, yellow, turquoise, None, None,
                    "The room is completely yellow green. Four exits,"
                    "one on each wall, leave the room. Lemon yellow is"
                    "to the north, yellow is to the east, turquoise is"
                    "to the south, and green is to the west."
                    )
orange_yellow = Room("The Orange Yellow Room", vworp, None, yellow, None, None,
                     "The room is orange yellow. Four exits, one"
                     "on each wall, leave the room. A strange,"
                     "portal-like door is to the north, orange is"
                     "to the east, yellow is to the south, and"
                     "lemon yellow is to the west."
                     )
orange = Room("The Orange Room", None, None, red, orange_yellow, None,
              "The room is completely orange. Three exits"
              "leave the room. Orange red is to the east, red is"
              "to the south, and orange yellow is to the west."
              )
orange_red = Room("The Orange Red Room", None, None, None, orange, None,
                  "The room is completely orange red. Two exits"
                  "leave the room. Scarlet red is to the south"
                  "and orange is to the west."
                  )
scarlet_red = Room("The Scarlet Red Room", orange_red, None, None, red, None,
                   "The room is completely scarlet red. Three exits"
                   "leave the room. Orange red is to the north, crimson"
                   "is to the south, and red is to the west."
                   )
crimson = Room("The Crimson Room", scarlet_red, vworp, None, scarlet, None,
               "The room is completely crimson. Four exits, one"
               "on each wall, leave the room. Scarlet red is"
               "to the north, a strange, portal-like door is"
               "to the east, magenta is to the south, and"
               "scarlet is to the west."
               )
magenta = Room("The Magenta Room", crimson, None, None, purple, None,
               "The room is completely magenta. Three exits"
               "leave the room. Crimson is to the north, purple"
               "magenta is to the south, and purple is to the"
               "west."
               )
purple_magenta = Room("The Purple Magenta Room", magenta, None, None, None, None,
                      "The room is completely violet. Two exits"
                      "leave the room. Magenta is to the north"
                      "and purple violet is to the west."
                      )
purple_violet = Room("The Purple Violet Room", purple, purple_magenta, None, None, None,
                     "The room is completely purple violet. Three exits"
                     "leave the room. Purple is to the north, purple"
                     "magenta is to the east, and blue violet is to the"
                     "west."
                     )
blue_violet = Room("The Blue Violet Room", violet, purple_violet, vworp, None, None,
                   "The room is completely blue violet. Four exits,"
                   "one on each wall, leave the room. Violet is to"
                   "the north, purple violet is to the east, a strange,"
                   " portal-like door is to the south, and blue is to"
                   "the west."
                   )
blue = Room("The Blue Room", cyan_blue, blue_violet, None, None, None,
            "The room is completely blue. Three exits leave the"
            "room. Cyan Blue is to the north, blue violet is to"
            "the east, and blueish cyan is to the west."
            )
blueish_cyan = Room("The Blueish Cyan Room", None, blue, None, None, None,
                    "The room is completely blueish cyan. Two"
                    "exits leave the room. Greenish cyan is to"
                    "the north, and blue is to the east."
                    )
greenish_cyan = Room("The Greenish Cyan Room", None, cyan_blue, blueish_cyan, None, None,
                     "The room is completely greenish cyan. Three exits"
                     "leave the room. Blueish green is to the north, cyan"
                     "blue is to the east, and blueish cyan is to the"
                     "south."
                     )
blueish_green = Room("The Blueish Green Room", None, turquoise, greenish_cyan, vworp, None,
                     "The room is completely blueish green. Four exits,"
                     "one on each wall, leave the room. Green is to the"
                     "north, turquoise is to the east, greenish cyan is"
                     "to the south, and a strange, portal-like door is to"
                     "the west."
                     )
green = Room("The Green Room", None, yellow_green, blueish_green, None, None,
             "The room is completely green. Three exits leave"
             "the room. Sap green is to the north, yellow"
             "green is to the east, and blueish green is to the"
             "south."
             )
sap_green = Room("The Sap Green Room", None, None, green, None, None,
                 "The room is completely sap green. Two exits"
                 "leave the room. Lemon yellow is to the east, and"
                 "green is to the south."
                 )
lemon_yellow = Room("The Lemon Yellow Room", None, orange_yellow, yellow_green, sap_green, None,
                    "The room is completely lemon yellow. Three exits"
                    "leave the room. Orange yellow is to the east,"
                    "yellow green is to the south, and sap green is to"
                    "the west."
                    )

vworp.vworp = white
white.north = yellow
white.east = scarlet
white.south = violet
white.west = turquoise
yellow.north = orange_yellow
yellow.east = red
yellow.west = yellow_green
scarlet.north = red
scarlet.east = crimson
scarlet.south = purple
violet.east = purple
violet.south = blue_violet
violet.west = cyan_blue
turquoise.north = yellow_green
turquoise.south = cyan_blue
turquoise.west = blueish_green
red.north = orange
red.east = scarlet_red
purple.east = magenta
purple.south = purple_violet
cyan_blue.south = blue
cyan_blue.west = greenish_cyan
yellow_green.north = lemon_yellow
yellow_green.west = green
orange_yellow.east = orange
orange_yellow.west = lemon_yellow
orange.east = orange_red
orange_red.south = scarlet_red
scarlet_red.south = crimson
crimson.south = magenta
magenta.south = purple_magenta
purple_magenta.west = purple_violet
purple_violet.west = blue_violet
blue_violet.west = blue
blue.west = blueish_cyan
blueish_cyan.north = greenish_cyan
greenish_cyan.north = blueish_green
blueish_green.north = green
green.north = sap_green
sap_green.east = lemon_yellow


# Controls
player = Player(white, [])

playing = True
directions = ['north', 'south', 'east', 'west', 'vworp']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            if next_room is None:
                raise AttributeError
            player.move(next_room)
        except AttributeError:
            print("This path does not exist")
    else:
        print("Command Not Found")
