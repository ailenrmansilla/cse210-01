import random

class Player:

    def __init__(self):
        self.points = 300
        self.playing = True

    def start_game(self):
        card = Card()
        while self.playing == True:
            first_number = card.number
            print(f'----Your card is {card.number}----')
            print(f'Time to guess!')
            guess = input(f'Next card is higher or lower? (Enter H or L): ').upper
            card = Card()
            new_number = card.number
            if new_number >= first_number:
                if guess == 'H':
                    print(f'You guessed correctly! The card\'s number was higher')
                    self.points += 100
                    print(f'You have {self.points} points')
                else:
                    print('Next card was ',new_number)
                    self.points -= 75
                    print(f'You have {self.points} points')
            elif new_number <= first_number:
                if guess == 'L':
                    print(f'You guessed correctly! The card\'s number was lower')
                    self.points += 100
                    print(f'You have {self.points} points')
                else:
                    print('Next card was ',new_number)
                    self.points -= 75
                    print(f'You have {self.points} points')
            if self.points > 0:
                play_again = input('Play again? (Enter Y/N): ').upper()
                if play_again == 'N':
                    self.playing = False
                    print('----Thanks for playing!----')
            else:
                print('-----GAME OVER-----')

    
class Card:
    def __init__(self): 
        self.number = random.randint(1,13)

player = Player()
player.start_game()