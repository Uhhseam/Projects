import math
import random

def main():
    lower, upper = check()
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
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
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next Time!")

def check():
    lower = (input("Enter Lower bound: "))
    upper = (input("Enter Upper bound: "))

    lowerC = isinstance(lower, int)
    upperC = isinstance(upper, int)
    if lowerC and upperC == True:
        value = "correct"
    else:
        value = "incorrect"
        while value == "incorrect":
            if lower and upper == False:
                print("Invalid option, Please input an Integer")
                lower = (input("Enter Lower bound1: "))
                upper = (input("Enter Upper bound1: "))
            elif lower and upper == True:
                value = "correct"
    
    
    return lower, upper
    

def loop():
    again = "y"
    while again == "y":
        main()
        again = input("Enter 'y' to play again or 'n' to quit: ")

loop()