import math
import random

def main():
    lower, upper = lowerUpperCheck()
    x = random.randint(lower, upper)
    print("\n\tYou only have",
            round(math.log(upper - lower + 1,2)),
            "chances to guess the integer! \n")

    count = 0

    while count < math.log(upper - lower + 1,2):
        count += 1
        guess = int(input("Guess a number: "))

        if x == guess:
            print("Congratulations you did it in ",
                count, " try")
            break
        elif x > guess:
            print("You guessed to small!")
        elif x < guess:
            print("You guessed too high!")

    if count >= math.log(upper - lower + 1,2):
        print("The number is %d" % x)
        print("\n\tBetter Luck Next Time!")

def lowerUpperCheck():
    value1 = value2 = "incorrect"
    while value1 == "incorrect":
        try:
            lower = int(input("Enter Lower bound number: "))
        except:
            print("\nInvalid option, Please input an Integer\n")
        else:
            value1 = "correct"
    while value2 == "incorrect":
        try:
            upper = int(input("Enter Upper bound number: "))
        except:
            print("\nInvalid option, Please input an Integer\n")
        else:
            value2 = "correct"
    return lower, upper

def numberCheck():
    value = "incorrect"
    while value == "incorrect":
        try:
            guess = int(input("Guess a number: "))
        except:
            print("\nInvalid option, Please input an Integer\n")
        else:
            value = "correct"
    return guess
def loop():
    print("Welcome to the number guessing game!\n")
    again = "y"
    while again == "y":
        main()
        again = input("\nEnter 'y' to play again or 'n' to quit: ")
        if again == 'y':
            print('\n')

loop()