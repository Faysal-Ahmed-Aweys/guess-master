import random

randNumber = print(random.randint(0,10))

def ask_for_a_number():
    while True:
        try:
            number = int(input("What is your number?: "))
            if type(number) == int:
                print("Okay")
                break
        except ValueError:
            print("You should input a number")
    return number


integer = ask_for_a_number()
print(f"Your number is {integer}")

def try_again_():
    while True:
        try_again = input("Would you like to try again? y/n ")
        if try_again.lower() == "y":
            integer = ask_for_a_number()
            print(f"Your number is {integer}")
        elif try_again.lower() == "n":
            print("Game over")
            break
        else:
            print("You should input either y/n")

try_again_()