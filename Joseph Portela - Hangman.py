import random
from hangman_addons import *

word_bank = ["avalanche", "big chungus", "chimera", "diameter", "evergreen", "florist", "garrison", "horoscope",
             "interior", "jubilee", "kiosk", "liaison", "menace", "negative", "obfuscate", "parabola", "quarrel",
             "remember", "salamander", "turquoise", "undermine", "variable", "wilderness", "xenophobia", "youthful",
             "zephyr"]

word = random.choice(word_bank)
guesses = 8
letters_guessed = []
letter_list = list(word)

while guesses > 0:
    hidden_word = []
    for letter in word:
        if letter in letters_guessed:
            hidden_word.append(letter)
        else:
            hidden_word.append("*")
    print("".join(hidden_word))

    current_guess = input("Type letter: ")
    letters_guessed.append(current_guess)

    if current_guess not in word:
        guesses -= 1
        print("Sorry, guess again.")
