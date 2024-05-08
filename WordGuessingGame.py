import random

name = (input("Enter your name to begin: "))

print("Good luck", name)
list1 = []

words = ('rainbow','computer','science','programing',
          'python', 'math', 'players', 'dell', 'laptop',
          'chrome','shibainu','lord','zombie')

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = len(word)

dash = "_"

failed = 0
for i in range(turns):
        list1 += dash
        print(list1)

'''if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

print()
guess = input("guess a character: ")
guesses += guess

if guess not in word:
    turns -= 1
    print("Wrong")
    print("You have ", + turns, "more guesses")

    if turns == 0:
        print("You Loose")'''