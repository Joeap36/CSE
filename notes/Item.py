class Item(object):
    def __init__(self, name):
        self.name = name


class Offense(Item):
    def __init__(self, name, durability):
        super(Offense, self).__init__(name)
        self.name = name
        self.durability = durability
