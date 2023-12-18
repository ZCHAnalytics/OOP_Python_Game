import random
# class definition
class HangMan:
    # class constructor with magic method
    def __init__(self, word_list, num_lives = 5):
        #attributes
        self.word_list = word_list
        self.num_lives = num_lives
        # attributes defined using other attributes
        self.word = random.choice(word_list)
        self.word_guessed = ["-" for letter in self.word]
        self.num_letters = len(set(self.word)) # unique letters 
        self.list_of_guesses = [] #empty list
 # methods - functions inside the class, what instances of the class can do   
    def check_guess(self, guess):
        guess = str.lower(guess)
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            # new
            for position, letter in enumerate(self.word):
                if letter == guess:
                    self.word_letters[position] = letter
            print(self.word_guessed)
            num_letters -= 1
        else:
            num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print('You have {num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Enter a letter: ')
            if not (guess.isalpha()) and (len(guess) == 1):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:    
                self.check_guess(guess)
                guess = self.list_of_guesses.append
my_game = HangMan(['banana', 'mango', 'cherry', 'apple', 'pear'])
my_game.ask_for_input()
     
   