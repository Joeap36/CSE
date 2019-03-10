class Shaggy(object):
    def __init__(self):
        self.universe = True
        self.power_percentage = 0
        self.ultra_instinct = False
        self.matt_from_wii_sports = True
        self.most_powerful_being = False

    def increase_power(self):
        if self.power_percentage < 100:
            self.power_percentage += 10
            print("Shaggy increased his power by 10 percent")
            print("Shaggy now has %d percent power" % self.power_percentage)
        elif self.power_percentage == 100:
            self.power_percentage = 9001
            self.ultra_instinct = True
            print("Shaggy's power level is over 9000")
            print("Shaggy has reached ultra instinct")
        else:
            print("Shaggy cannot increase his power further")

    def fight_matt(self):
        if self.ultra_instinct = True:
            self.matt_from_wii_sports = False
            self.most_powerful_being = True
            print("Shaggy fought Matt from Wii Sports and won. He is now the most powerful being")
        else:
            self.power_percentage = 0
            print("Shaggy fought Matt from Wii Sports and lost. His power level was reset to 0")
            
    def destroy_universe(self):
        if self.most_powerful_being = True:
            self.universe = False
            print("Shaggy has destroyed the universe. All that once was is gone")
        else:
            print("Shaggy is not yet strong enough to do so")
                  
