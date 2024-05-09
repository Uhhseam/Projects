import random

name = (input("Enter your name to begin: "))

print("Good luck", name)
list1 = []

words = ('rainbow','computer','science','programing',
          'python', 'math', 'players', 'dell', 'laptop',
          'chrome','shibainu','lord','zombie')

word = random.choice(words)

print("Guess the characters")

turns = len(word)
correct_guesses = ['_'] * turns
print(correct_guesses)

while '_' in correct_guesses:
    guess = input("Enter a character: ").lower()
    if not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue
    if guess in correct_guesses:
        print("You've already guessed that letter.")
        continue




'''list1 = "_" * turns
print('(', list1,')')

if failed == 0:
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