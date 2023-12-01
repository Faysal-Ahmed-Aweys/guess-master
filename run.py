import random

def generate_random_number():
    randNumber = int(random.randint(0, 10))
    return randNumber

def ask_for_a_number(randNumber):
    while True:
        try:
            number = int(input("Guess a number (it is between 0 and 10): "))
            if type(number) == int and number == randNumber:
                print("Okay, You're right. Well done!!")
                print(f"The number is {randNumber}")
                break
            elif type(number) == int and number < randNumber:
                print("Higher")
            elif type(number) == int and number > randNumber:
                print("lower")
        except ValueError:
            print("You should input a number")
    return number


def gameRules():
    print("""
                        Game Rules
                        ----------

    - The game rules are simple and straightforward.
    - The computer is thinking of a number, it will tell you the range.
    - Your job is to guess what the number is. 
    - If you guess a lower number, the computer will tell you higher which means 
      you need to guess a number higher than the number you guessed. 
    - If you guess a higher number, the computer will tell you lower which means 
      you need to guess a number lower than the number you guessed.
    - here is the catch though, you have only three chances to guess what the number is!

                    HAVE FUN!!!
    """)

    while True:
        start_game = input("Would you like to start the game? y/n ")
        if start_game.lower() == "y":
            generate_random_number()
            break
        elif start_game.lower() == "n":
            welcome()
            break
        else:
            print("You should input either y/n")


def welcome():
    print("""
    ~~~ Hello and welcome ~~~
    """)

    print("""
select an option:
1. Start game 
2. Game rules
    """)
    while True:
        try:
            chosen_option = int(input("type 1 or 2: "))
            type(chosen_option) == int
            if type(chosen_option) == int and chosen_option == 1:
                generate_random_number()
                break
            elif type(chosen_option) == int and chosen_option == 2:
                gameRules()
                break
        except ValueError:
            print("please enter a number")

welcome()
random_number = generate_random_number()
print(random_number)
integer = ask_for_a_number(random_number)

def try_again_():
    while True:
        try_again = input("Would you like to try again? y/n ")
        if try_again.lower() == "y":
            random_number = generate_random_number()
            print(random_number)
            ask_for_a_number(random_number)
        elif try_again.lower() == "n":
            print("game over")
            break
        else:
            print("You should input either y/n")

try_again_()