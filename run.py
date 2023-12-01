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
            print("You're done")
            break
        else:
            print("You should input either y/n")

try_again_()