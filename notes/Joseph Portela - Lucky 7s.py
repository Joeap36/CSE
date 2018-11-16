import random

ctotal = 15
mtotal = 15
rounds = 0
best_round = 0

while ctotal > 0:
    print("Your total: $%d" % ctotal)
    print("You bet $1")
    generated_number_1 = random.randint(1, 6)
    generated_number_2 = random.randint(1, 6)
    print("Your rolled %d and %d" % (generated_number_1, generated_number_2))
    roll = (generated_number_1 + generated_number_2)
    print("You rolled a %d" % roll)
    if roll != 7:
        ctotal -= 1
        print("You lost the bet")
    elif roll == 7:
        ctotal += 4
        print("You won the bet and got $5")
        if mtotal < ctotal:
            mtotal = ctotal
            best_round = rounds
    rounds += 1

if ctotal <= 0:
    print("You're bankrupt. You go home, tell your spouse and kids, and you live in poverty for the rest of your life.")
    print()
    print("Congratulations!")
    print("You could've stopped when you had $%d, but noooOOOooo." % mtotal)
    print("You just had to keep going for, let me check...")
    print("%d ROUNDS?! How long did that take?!" % rounds)
    print("Well, this is a programmed simulation so I guess it was instantaneous, but STILL!")
    print("You should be ashamed.")
