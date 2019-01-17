import random
from hangman_addons import *

words = ["avalanche", "big chungus", "chimera", "diameter", "evergreen", "florist", "garrison", "horoscope", "interior",
         "jubilee", "kiosk", "liaison", "menace", "negative", "obfuscate", "parabola", "quarrel", "remember",
         "salamander", "turquoise", "undermine", "variable", "wilderness", "xenophobia", "youthful", "zephyr"]


word = random.choice(words)
guesses = 6
