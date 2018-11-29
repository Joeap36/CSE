import random

words = ["avalanche", "breach", "chimera", "diameter", "evergreen", "florist", "garrison", "horoscope", "interior",
         "jubilee", "katana", "liaison", "menace", "negative", "obfuscate", "parabola", "quarrel", "remember",
         "salamander", "turquoise", "undermine", "variable", "wilderness", "xenophobia", "youthful", "zephyr"]

def wrong_0():
    print("------|")
    print(" |    |")
    print(" |")
    print(" |")
    print(" |")
    print(" |")
    print("---")
def wrong_1():
    print("------|")
    print(" |    |")
    print(" |   ( )")
    print(" |")
    print(" |")
    print(" |")
    print("---")
def wrong_2():
    print("------|")
    print(" |    |")
    print(" |   ( )")
    print(" |    |")
    print(" |    |")
    print(" |")
    print("---")
def wrong_3():
    print("------|")
    print(" |    |")
    print(" |   ( )")
    print(" |   /|")
    print(" |    |")
    print(" |")
    print("---")
def wrong_4():
    print("------|")
    print(" |    |")
    print(" |   ( )")
    print(" |   /|\ ")
    print(" |    |")
    print(" |")
    print("---")
def wrong_5():
    print("------|")
    print(" |    |")
    print(" |   ( )")
    print(" |   /|\ ")
    print(" |    |")
    print(" |   /")
    print("---")
def wrong_6():
    print("------|")
    print(" |    |")
    print(" |   ( )")
    print(" |   /|\ ")
    print(" |    |")
    print(" |   / \ ")
    print("---")

def main():
    rand_word = random.choice(words)
    print("Welcome to Hangman!")

main()
