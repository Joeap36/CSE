import random


def main():
    generated_number = random.randint(1, 10)

    user_guess = 0
    turns_used = 0
    win = False

    while turns_used != 5 and not win:
        user_guess = int(input("Guess a number from 1 to 10"))
        if user_guess != 0 and user_guess != generated_number:
            print("Incorrect")
            turns_used += 1
            if generated_number < user_guess:
                print("Lower")
            elif generated_number > user_guess > 0:
                print("Higher")
            user_guess = 0
        elif user_guess == generated_number:
            print("You Win!")
            win = True

    if turns_used == 5:
        print("Game Over")
    next_game = input("Play again?")
    


main()
