import random


class Hangman: 
    """
    A Hangman Game where a player guesses letters to reveal a mystery word.
    
    Parameters:
    ----------
        word_list (list): List of words for the game.
        num_lives (int): Numbers of attempts allowed.
        
    Attributes:
    ----------
        self.word (str): The word to be guessed picked randomly from the word_list.
        self.word_guessed (list): 
            A list of the letters of the word, with '_' for each letter not yet guessed.
            For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
            If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
        self.num_lives (int): Numbers of attempts allowed. Deafult can be changed in the init method.
        self.list_guesses (list): A list of the letters that have already been tried.

    Methods:
    -------
        check_guess(guess): Checks if the guess which a letter provided by the user is in the word. 
        ask_for_input(): Asks for player's input, checkes if it is a single, alphabetical character (not a number) and that it was not used before.
    """

    def __init__(self, word_list, num_lives = 5):
        """ 
        Constructor method to initialise class attributes.
        
        Parameters:
        ----------
            self (Hangman): The instance of the Hangman class.
            word_list (list): List of words for the game. 
            num_lives (int): Number of attempts allowed. Default is 5.

        Attributes: 
        ----------
            self.word (string): Randomly chosen word.
            self.word_list (list): List of words for the game.
            self.num_lives (int): Remaining attempts.
            self.word_guessed (list): List of letters in the word with '_' for unrevealed letters.
            self.num_letters (length): Number of unique letters in the chosen word.
            self.list_of_guesses (list): List of correctly guessed letters.              
        """
        
        self.word_list = word_list 
        self.num_lives = num_lives 
        self.word = random.choice(word_list) 
        self.word_guessed = ["_" for letter in self.word] 
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = []  
        print(f'\nThe mistery word has {len(self.word)} characters')
        print(f'\n {self.word_guessed}')
        

    def check_guess(self, guess) -> None: 
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.
        If the letter is in the word, it replaces the '_' in word_guessed with the letter.
        If it is not, it decreases the number of lives by 1.

        Parameters:
        ----------
            guess (str): Player's guess to be checked.
        """
        guess = str.lower(guess) 
        if guess in self.word:
            print(f'\nGood guess! {guess} is in the word.')
            for position, letter in enumerate(self.word): 
                if letter == guess: 
                    self.word_guessed[position] = letter # If the guess is correct, replaces dashes with a correctly guessed letter.
            self.num_letters -= 1 # Removes the correctly guessed letter from the list of letters to be guessed.
        else:
            self.num_lives -= 1 # If the guess is incorrect, reduces number of lives by 1. 
            print(f'\nSorry, {guess} is not in the word')
            print(f'\nYou have {self.num_lives} lives left.')
    

    def ask_for_input(self):
        """ 
        Asks for user's input, checks if it is a single, alphabetical character (not a number) and that it was not used before.
        """
        while True:
            guess = input('\nPlease, enter a letter: ') # Asks the user to input a letter.
            if not (guess.isalpha() and len(guess) == 1): # Checks if the user's input is single alphabetical (not a number) character.
                print('\nInvalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses: # Checks if the user's input has previously been used. 
                print('\nYou already tried that letter!')
                print(f'\n {self.word_guessed}')
            else:
                self.list_of_guesses.append(guess) # Updates the list of unique letters inputted by the user.
                self.check_guess(guess) # Checks if the inputted letter is in the chosen word.
                print('\nCurrent word: ', self.word_guessed) # Print the updated list of dashes to show the progress of the game. 
                break


def play_game(word_list):
    """
    Initialises the game and plays it, counting the number of remaining attempts. 
    Once the remaining attempts equal zero, it informs the player that they lost the game.
    It also checks if all the unique letters in the word have been guessed and informs the player if they won.

    Parameters:
    ----------
        word_list (list): List of words for the game.
    """
    num_lives = 5 
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0: # Once the number of used lives reaches zero, print messages that the user lost the game.   
            print(f'\nYou lost! The mystery word was {game.word}')
            break
        elif game.num_letters > 0: # Continues game if there are still lives available.
            game.ask_for_input()
        else: # Print message to congratulate the use with winning the game. 
            print('\nCongratulations. You won the game!')
            break


if __name__ == '__main__':
    # Run this code only if it runs directly. #
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
