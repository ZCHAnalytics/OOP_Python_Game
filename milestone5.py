import random
# class definition
class HangMan: 
    # class constructor with magic method
    def __init__(self, word_list, num_lives = 5): # TODO 2
        self.word_list = word_list  
        self.num_lives = num_lives  
        # attributes defined using other attributes
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(set(self.word)) # unique letters 
        self.list_of_guesses = [] #empty list
        print("The mistery word has", self.num_letters, "characters")
        print(self.word_guessed)
        pass # from template 
 # methods - functions inside the class, what instances of the class can do      
    def check_guess(self, guess) -> None: #TODO 3 ## checks if the letter inputted is in the hidden word
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
        pass #template

    def ask_for_input(self):
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
        pass #from template

def play_game(word_list):
    num_lives = 5
    game = HangMan(word_list, num_lives)
    while True: #TODO 4
        if game.num_lives == 0:
            print(f'You lost! the word was {game.word}')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            print(game.num_lives)
        else: 
            print('Congratulations. You won the game!')
            print(game.num_letters)
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)