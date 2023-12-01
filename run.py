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