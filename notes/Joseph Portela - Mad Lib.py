print("Welcome to Your Very Own Mad Lib, otherwise known as YVOML! Please answer each prompt.")
print()

# Inputs

Plural_noun_1 = input("Enter a plural noun. ")
Plural_noun_2 = input("Enter another plural noun. ")
Number_1 = int(input("Enter a number. "))
Ing_verb_1 = input("Enter a verb ending in ing. ")
Plural_noun_3 = input("Enter another plural noun.")
Name_1 = input("Enter a name.")
Adjective_1 = input("Enter an adjective")
Noun_1 = input("Enter a noun.")
Plural_noun_4 = input("Enter yet another plural noun.")
Noun_2 = input("Enter another noun.")
Number_2 = int(input("Enter another number."))
Plural_noun_5 = input("Enter another plural noun.")

# Story

print("Great! YVOML is now complete, here is the result:")
print("Welcome to the Cult of %s, we believe that %s are really gods in disguise!" % (Plural_noun_1, Plural_noun_2))
print("We hold services %d days a week, and each service we hold a holy %s." % (Number_1, Ing_verb_1))
print("If you're interested, read our holy book, written by the God of %s." % Plural_noun_3)
print("I highly recommend the book of %s, it includes the famous story of the %s %s." % (Name_1, Adjective_1, Noun_1))
print("In the cult of %s, our goal is eternal dedication to the one great god of %s." % (Plural_noun_1, Plural_noun_4))
print("All who follow him will receive a %s in the afterlife, as well as %d %s." % (Noun_2, Number_2, Plural_noun_5))
print("Wait, Where are you going? Please stay! I have... so much more to tell you... *sigh* Next house then...")
