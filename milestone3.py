import random
# create a list of word for the game
word_list = ['banana', 'mango', 'cherry', 'apple', 'pear']
word = random.choice(word_list) # selecting a random word from the list
print(word)

# create two functions
def check_guess(guess): # function for checking if a guessed letter belongs to the hidden word
    guess = str.lower(guess)
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

def ask_for_input(): # function for checking if the guessed letter is an alphabatetical, single character
    while True:
        guess = input('Enter a letter: ')
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)
ask_for_input()
