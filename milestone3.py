import random

word_list = ['banana', 'mango', 'cherry', 'apple', 'pear']
word = random.choice(word_list) 
print(word)

# create functions
def check_guess(guess):
    guess = str.lower(guess)
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

def ask_for_input():
    while True:
        guess = input('Enter a letter: ')
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)
ask_for_input()
