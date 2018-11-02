import random
a = (random.randint(1, 10))  # a = Random number

b = 0  # b = User's guess
c = 0  # c = Number of turns used

while b != (0, a):
    print("Incorrect")
    c += 1


while c == 5:
    print("Game Over")


while 0 < a < b:
    print("Lower")
    b = 0


while 0 < b < a:
    print("Higher")
    b = 0

