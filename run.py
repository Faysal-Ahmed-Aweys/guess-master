import random
from os import system


def clear():
    system('clear')


def try_again_():
    while True:
        try_again = input("Would you like to try again? y/n\n")
        if try_again.lower() == "y":
            clear()
            random_number = generate_random_number()
            ask_for_a_number(random_number)
        elif try_again.lower() == "n":
            clear()
            welcome()
            break
        else:
            print("You should input either y/n")


def ask_for_a_number(rand_number):
    clear()
    attempts = 3
    print(f"{attempts} chance(s) left")
    while True:
        try:
            number = int(input("Guess a number (between 0 and 10):\n"))
            if type(number) == int and number == rand_number:
                print("You got it, Well done!!")
                print(f"The number is {rand_number}")
                try_again_()
            elif type(number) == int and number < rand_number and attempts != 1:
                attempts -= 1
                print("Higher")
                print(f"{attempts} chance(s) left")
            elif type(number) == int and number > rand_number and attempts != 1:
                attempts -= 1
                print("lower")
                print(f"{attempts} chance(s) left")
            elif attempts <= 1:
                attempts -= 1
                print(f"{attempts} chance(s) left")
                print("Game over")
                print(f"The number is {rand_number}")
                try_again_()
        except ValueError:
            print("You should input a number")


def generate_random_number():
    rand_number = int(random.randint(0, 10))
    return rand_number


def game_rules():
    print("""
                        Game Rules
                        ----------

- The game rules are simple and straightforward.
- The computer is thinking of a number and it will tell you the range.
- Your job is to guess what the number is.
- If you guess a lower number, the computer will tell you higher which means
  you need to guess a number higher than the number you guessed.
- If you guess a higher number, the computer will tell you lower which means
  you need to guess a number lower than the number you guessed.
- If you guess the right number you win!
- You have only three chances to guess what the number is!

                    HAVE FUN!!!
    """)

    while True:
        start_game = input("Would you like to start the game? y/n\n")
        if start_game.lower() == "y":
            clear()
            random_number = generate_random_number()
            ask_for_a_number(random_number)
            break
        elif start_game.lower() == "n":
            clear()
            welcome()
            break
        else:
            print("You should input either y/n")


def welcome():

    row1 = "╔═╗┬ ┬┌─┐┌─┐┌─┐  ┌┬┐┬ ┬┌─┐  ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐"
    row2 = "║ ╦│ │├┤ └─┐└─┐   │ ├─┤├┤   ││││ ││││├┴┐├┤ ├┬┘"
    row3 = "╚═╝└─┘└─┘└─┘└─┘   ┴ ┴ ┴└─┘  ┘└┘└─┘┴ ┴└─┘└─┘┴└─"

    print(row1.center(50))
    print(row2.center(50))
    print(row3.center(50))

    print("""
SELECT AN OPTION:
1. START GAME
2. GAME RULES
    """)

    while True:
        try:
            chosen_option = int(input("Type 1 or 2:\n"))
            if type(chosen_option) == int and chosen_option == 1:
                random_number = generate_random_number()
                ask_for_a_number(random_number)
                break
            elif type(chosen_option) == int and chosen_option == 2:
                game_rules()
                break
        except ValueError:
            print("Please type 1 or 2")


welcome()
