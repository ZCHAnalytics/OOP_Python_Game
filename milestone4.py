import random
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives
        self.word_list = ['banana', 'mango', 'cherry', 'apple', 'pear']
        self.word = random.choice(word_list) 
        self.word_guessed = list(self.word)
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = 0

    def check_guess(self, guess):
        guess = str.lower(guess)
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

    def ask_for_input(self):
        while True:
            guess = str(input('Enter a letter: '))
            if not (guess.isalpha()) and (len(guess) == 1):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:    
                self.check_guess(guess)
                self.list_of_guesses.append()
    ask_for_input()
