class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, vworp=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.vworp = vworp


vworp = Room("Vworp", None, None, None, None, None)
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
crimson = Room("The Crimson Room", scarlet_red, vworp, magenta, scarlet, None)
magenta = Room("The Magenta Room", crimson, None, purple_magenta, purple, None)
purple_magenta = Room("The Purple Magenta Room", magenta, None, None, purple_violet, None)
purple_violet = Room("The Purple Violet Room", purple, purple_magenta, None, blue_violet, None)
blue_violet = Room("The Blue Violet Room", violet, purple_violet, vworp, blue, None)
blue = Room("The Blue Room", cyan_blue, blue_violet, None, blueish_cyan, None)
blueish_cyan = Room("The Blueish Cyan Room", greenish_cyan, blue, None, None, None)
greenish_cyan = Room("The Greenish Cyan Room", blueish_green, cyan_blue, blueish_cyan, None, None)
blueish_green = Room("The Blueish Green Room", green, turquoise, greenish_cyan, vworp, None)
green = Room("The Green Room", sap_green, yellow_green, blueish_green, None, None)
sap_green = Room("The Sap Green Room", None, lemon_yellow, green, None, None)
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

