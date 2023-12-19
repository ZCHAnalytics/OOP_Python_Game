import random
# class definition
class HangMan: 
    """ 
    This class represents a game.
    Attributes: 
    word_list(list): list of words from which a random word is selected.
    num_lives (int): numbers of lives or attempts that a user has before game ends.
    """
    # class constructor with magic method
    def __init__(self, word_list, num_lives = 5): # TODO 2
        """ 
        This method to construct initial class attributes and then additional attributes using these initial attributes:
        word_list(list): list of words from which a random word is selected.
        num_lives (int): numbers of lives or attempts that a user has before game ends.
        word(string): a randomly chosen word from the list of words.
        word_guessed(list): a list of dashes with each dash representing a letter in the chosen word.
        num_letters(length): number of unique letters in a chosen word.
        list_of_guesses(list): a list of correctly guessed letters. 
        This method picks a random word from the list of words and returns it as a list of empty spaces (dashes). 
        """
        self.word_list = word_list  
        self.num_lives = num_lives  
        # attributes defined using other attributes
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word)) # unique letters 
        self.list_of_guesses = [] #empty list
        print("The mistery word has", len(self.word), "characters")
        print(self.word_guessed)
        pass # from template 
 # methods - functions inside the class, what instances of the class can do      
    def check_guess(self, guess) -> None: #TODO 3 ## checks if the letter inputted is in the hidden word
        """
        This method checks if the letter inputted by the user belongs to the hidden word. 
        Method's parameter is user's input called guess. 
        The method also informs the user if the guess was correct.
         The method also informs how many lives the user has after an incorrect guess.
        """
        guess = str.lower(guess) 
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            # new
            for position, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[position] = letter #TODO 3
            self.num_letters -= 1 #TODO 3
        else:
            self.num_lives -= 1 #TODO 3
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left.')
        pass # from hangman.py template

    def ask_for_input(self):
        """
        This method asks for user's input, validates if the input is a single, alphabetical character and not a number.
        It also checks if the user has already guessed the letter.  
        """
        while True: #TODO 1 
            guess = input('Enter a letter: ') #TODO 1
            if not (guess.isalpha() and len(guess) == 1): #TODO1 
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses: #TODO 2
                print('You already tried that letter!')
                print(self.word_guessed) # checking
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess) #TODO 3
                break
        # pass #from template

def play_game(word_list):
    """
    This method takes word_list as a parameter.
    It counts how many attempts the user has. Once the remaining attempts equal zero, it informs the user
    that they lost the game.
    It also counts if all the unique letters in the word have been guessed and informs the user 
    if they won.
    """
    num_lives = 5
    game = HangMan(word_list, num_lives)
    while True: #TODO 4
        if game.num_lives == 0:
            print(f'You lost! the word was {game.word}')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else: 
            print('Congratulations. You won the game!')
            break
if __name__ == '__main__':
    """
    Statement that runs this code only if it runs directly.
    """
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)