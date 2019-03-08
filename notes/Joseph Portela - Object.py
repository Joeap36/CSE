class Shaggy(object):
    def __init__(self):
        self.universe = True
        self.power_percentage = 1
        self.god = False
        self.matt_from_wii_sports = True
        self.most_powerful_being = False

    def increase_power(self):
        if self.power_percentage < 100:
            self.power_percentage += 5
            print("Shaggy increased his power by 5 percent")
            print("Shaggy now has %d percent power" % self.power_percentage)
        elif self.power_percentage == 100:
            self.power_percentage = 9001
            print("Shaggy's power level is over 9000")
        else:
            print("Shaggy cannot increase his power further")

    def