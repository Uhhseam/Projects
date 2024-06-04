import random

name = (input("Enter your name to begin: "))

print("Good luck! ", name)

words = ('rainbow','computer','science','programing',
          'python', 'math', 'players', 'dell', 'laptop',
          'chrome','shibainu','lord','zombie')

word = random.choice(words)
print(word)

print("Guess the characters")

turns = len(word)
correct_guesses = ['_' for _ in word]

def display_guessed_word():
    print(' '.join(correct_guesses))

def guess_letters(letter):
    global turns
    correct_guess = False
    for index, char in enumerate(word):
        if char == letter:
            correct_guesses[index] = letter
            correct_guess = True
    
    if correct_guess:
        print("Correct!")
    else:
        print("Incorrect!")
        turns -= 1
        print("You have", turns, "tries left")
        if turns == 0:
            print("Game over! The word was:", word)

while '_' in correct_guesses and turns > 0:
    display_guessed_word()
    guess = input("Enter a character: ").lower()
    if guess == word:
        print(name + ", You guessed the word correctly!\n with " + str(turns) + " tries left!")
        correct_guesses = [_ for _ in word]
    elif len(guess) == 1 and guess.isalpha():
        guess_letters(guess)
    else:
        print("Please enter a single alphabet")
