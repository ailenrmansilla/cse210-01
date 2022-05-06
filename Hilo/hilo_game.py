#Player: initialize it with 300 points. Guess if next card will be higher or lower. Can choose if keep playing or not.
#Earns 100 if guess correctly, looses 75 if doesnt. If 0, game over
#Card: is displayed. Represented with a number between 1 and 13.

#many classes and method comments
#game play and game over displays
import random

class Player:

    def __init__(self):
        self.points = 300
        self.playing = True

    def start_game(self):
        pass
    
class Card:
    def __init__(self): 
        self.number = random.randint(1,13)


player = Player()
card = Card()
while player.playing == True:
    first_number = card.number
    print(f'----Your card is {card.number}----')
    print(f'Time to guess!')
    guess = input('Higher or lower? (Enter H or L): ').upper
    card = Card()
    new_number = card.number
    #fix the conditionals
    if new_number >= first_number and guess == 'H':
        print(f'You guessed correctly! The card\'s number was higher')
    elif new_number <= first_number and guess == 'L':
        print(f'You guessed correctly! The card\'s number was lower')
    else:
        print('You didnt guess correctly!')
    play_again = input('Play again? (Enter Y/N) ')
    if play_again == 'N':
        player.playing = False
    