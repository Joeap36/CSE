class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, vworp=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.vworp = vworp
