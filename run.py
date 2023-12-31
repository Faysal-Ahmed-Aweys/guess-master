import random
from os import system
import emoji


def clear():
    """
    Clears the terminal whenever it is called.
    """

    system('clear')


def try_again_():
    """
    Asks the user whether they would like to try again.
    handles and validates user input. Guides user if user input is wrong.
    based on user input, start_game or welcome function is called.
    """

    while True:
        try_again = input("Would you like to try again? y/n\n")
        if try_again.lower() == "y":
            clear()
            random_number = generate_random_number()
            start_game(random_number)
        elif try_again.lower() == "n":
            clear()
            welcome()
        else:
            print("You should input either y/n")


def start_game(rand_number):
    guessed_list = []
    """
    Takes in random number from generate_random_number function.
    Resets attempts to guess the number.
    Asks the player to guess a number.
    Handles and validates user input.
    If the player wins or loses, try_again function is called.
    """
    clear()
    attempts = 3
    print(f"{attempts} chance(s) left\n")
    while True:
        try:
            number = int(input("Guess a number (between 0 and 10):\n"))
            if isinstance(number, int) and number == rand_number:
                print(emoji.emojize
                      ("\nYou got it, Well done!! "
                       ":smiling_face_with_sunglasses::thumbs_up:"))
                print(f"The number is {rand_number}\n")
                try_again_()
            elif number in guessed_list:
                print(f"\nyou already guessed {number}")
                print(f"{attempts} chance(s) left\n")
            elif isinstance(number, int) and \
                    number < rand_number and attempts > 1:
                if 10 >= number >= 0:
                    attempts -= 1
                    print(emoji.emojize("\nGuess a higher number :up_arrow:"))
                    guessed_list.append(number)
                    print(f"{attempts} chance(s) left\n")
                else:
                    print("the number is not between 0 and 10")
                    print(f"{attempts} chance(s) left\n")
            elif isinstance(number, int) and \
                    number > rand_number and attempts > 1:
                if 10 >= number >= 0:
                    attempts -= 1
                    print(emoji.emojize("\nGuess a lower number :down_arrow:"))
                    guessed_list.append(number)
                    print(f"{attempts} chance(s) left\n")
                else:
                    print("the number is not between 0 and 10")
                    print(f"{attempts} chance(s) left\n")
            elif attempts <= 1:
                if 10 >= number >= 0:
                    attempts -= 1
                    print(f"\n{attempts} chance(s) left")
                    print(emoji.emojize("Game over :pensive_face:"))
                    print(f"The number is {rand_number}\n")
                    try_again_()
                else:
                    print("the number is not between 0 and 10")
                    print(f"{attempts} chance(s) left\n")
        except ValueError:
            print("You should input a number")


def generate_random_number():
    """
    Generates a random number between 0 and 10 inclusive.
    """

    rand_number = int(random.randint(0, 10))
    return rand_number


def game_rules():
    """
    Displays game rules and asks the user whether to start the game or not.
    Handles and verifies user input. raises an error if user input is wrong.
    based on what option is chosen,
    the start_game or welcome function is called.
    """

    print("""
                        Game Rules
                        ----------

1. You have to guess a number within a certain range
   (for example between 0 and 10 inclusive).
2. If you guess a lower number, "guess a higher number" will be displayed
   which means you need to guess a number higher than the number you guessed.
3. If you guess a higher number, "guess a lower number" will be displayed
   which means you need to guess a number lower than the number you guessed.
4. You cannot guess the same number twice.
5. You cannot guess a number outside of the range.
6. If you guess the right number you win!
7. If you fail to guess the number after
   a specified number of tries/chances you lose!


                    HAVE FUN!!!
    """)

    while True:
        game_start = input("Would you like to start the game? y/n\n")
        if game_start.lower() == "y":
            clear()
            random_number = generate_random_number()
            start_game(random_number)
        elif game_start.lower() == "n":
            clear()
            welcome()
        else:
            print("You should input either y/n")


clear()


def welcome():
    """
    Displays title of the game and options of start game and game rules.
    Handles and verifies user input. raises an error if user input is wrong.
    based on what option is chosen,
    the start_game or game_rules function is called.
    """
    row1 = "╔═╗┬ ┬┌─┐┌─┐┌─┐  ┌┬┐┬ ┬┌─┐  ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐"
    row2 = "║ ╦│ │├┤ └─┐└─┐   │ ├─┤├┤   ││││ ││││├┴┐├┤ ├┬┘"
    row3 = "╚═╝└─┘└─┘└─┘└─┘   ┴ ┴ ┴└─┘  ┘└┘└─┘┴ ┴└─┘└─┘┴└─"

    print(row1.center(73))
    print(row2.center(73))
    print(row3.center(73))

    print(emoji.emojize(":man::speech_balloon: Hello there! "
                        "up for a challenge?").center(72))

    print("""
SELECT AN OPTION:

1. START GAME
2. GAME RULES
    """)

    while True:
        try:
            chosen_option = int(input("Type 1 or 2:\n"))
            if isinstance(chosen_option, int) and chosen_option == 1:
                random_number = generate_random_number()
                clear()
                start_game(random_number)
            elif isinstance(chosen_option, int) and chosen_option == 2:
                clear()
                game_rules()
        except ValueError:
            print("Please type 1 or 2")


welcome()
