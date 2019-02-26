class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, vworp=None, description=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.vworp = vworp
        self.description = description

class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

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
white = Room("The White Room", None, None, None, None, None)
yellow = Room("The Yellow Room", None, None, white, None, None)
scarlet = Room("The Scarlet Room", None, None, None, white, None)
violet = Room("The Violet Room", white, None, None, None, None)
turquoise = Room("The Turquoise Room", None, white, None, None, None)
red = Room("The Red Room", None, None, scarlet, yellow, None)
purple = Room("The Purple Room", scarlet, None, None, violet, None)
cyan_blue = Room("The Cyan Blue Room", turquoise, violet, None, None, None)
yellow_green = Room("The Yellow Green Room", None, yellow, turquoise, None, None)
orange_yellow = Room("The Orange Yellow Room", vworp, None, yellow, None, None)
orange = Room("The Orange Room", None, None, red, orange_yellow, None)
orange_red = Room("The Orange Red Room", None, None, None, orange, None)
scarlet_red = Room("The Scarlet Red Room", orange_red, None, None, red, None)
crimson = Room("The Crimson Room", scarlet_red, vworp, None, scarlet, None)
magenta = Room("The Magenta Room", crimson, None, None, purple, None)
purple_magenta = Room("The Purple Magenta Room", magenta, None, None, None, None)
purple_violet = Room("The Purple Violet Room", purple, purple_magenta, None, None, None)
blue_violet = Room("The Blue Violet Room", violet, purple_violet, vworp, None, None)
blue = Room("The Blue Room", cyan_blue, blue_violet, None, None, None)
blueish_cyan = Room("The Blueish Cyan Room", None, blue, None, None, None)
greenish_cyan = Room("The Greenish Cyan Room", None, cyan_blue, blueish_cyan, None, None)
blueish_green = Room("The Blueish Green Room", None, turquoise, greenish_cyan, vworp, None)
green = Room("The Green Room", None, yellow_green, blueish_green, None, None)
sap_green = Room("The Sap Green Room", None, None, green, None, None)
lemon_yellow = Room("The Lemon Yellow Room", None, orange_yellow, yellow_green, sap_green, None)

vworp.vworp = white
white.north = yellow
white.west = scarlet
white.south = violet
white.east = turquoise
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

player = Player(white)

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
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Found")
