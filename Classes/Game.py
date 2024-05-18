from Classes.Player import *
from Classes.Bank import *
from Classes.Deck import *
from Classes.Hand import *
import time
import os


class Game:
    def __init__(self, decks:list, player:Player, bank:Bank) -> None:
        # List of decks
        self.decks = decks

        # Cards in game
        self.cards_in_game = self.get_all_cards_list()

        # Others
        self.player = player
        self.bank = bank
        
    
    def get_all_cards_list(self):
        all_cards = []
        
        for deck in self.decks:
            size = deck.get_deck_len()
            deck = deck.get_deck()

            for i in range(0, size):
                all_cards.append(deck[i])
        
        return all_cards
    

    def get_cards_quantity(self) -> int:
        return len(self.cards_in_game)
    

    def get_random_card(self):
        size = self.get_cards_quantity()

        index = np.random.randint(0, size)

        card = self.cards_in_game[index]
        del(self.cards_in_game[index])

        return card
    

    def inicialize_game(self) -> bool:
        self.player.clear_hand()
        self.bank.clear_hand()

        if len(self.decks) == 0:
            return False
        else:
            size = len(self.decks)

            # Player begins with 2 cards
            self.player.add_card(self.get_random_card())
            self.player.add_card(self.get_random_card())

            # Bank begins with 1 card
            self.bank.add_card(self.get_random_card())

            # Initial print
            self.print_game()

            return True
    
    
    def print_game(self):
        print('====================================')
        print(f'Cards Quantity: {self.get_cards_quantity()}\n')
        print(self.bank)
        print('')
        print(self.player)
        print('====================================')
        
    
    def the_game(self):
        # To control when the game have to stop
        p_continue = ''
        game_end = 0
        draw = 0
        valid = 0

        while not(game_end) and self.get_cards_quantity() > 5:
            self.inicialize_game()

            while not(game_end):
                p_answer = input('Hit [h] or Stay [s]: ')
            
                match p_answer.lower():
                    case 'h':
                        self.player.add_card(self.get_random_card())
                        os.system('cls')
                        self.print_game()

                        if self.player.get_hand_value() > 21:
                            game_end = 1

                    case 's':
                        while self.bank.get_hand_value() <= self.player.get_hand_value() and self.get_cards_quantity() > 0 and self.bank.get_hand_value() != 21:
                            self.bank.add_card(self.get_random_card())
                            time.sleep(0.7)
                            os.system('cls')
                            self.print_game()
                            
                        if self.bank.get_hand_value() == self.player.get_hand_value():
                            draw = 1

                        game_end = 1
                
                    case '-1':
                        game_end = 1

                    case _:
                        print('\nNot a valid answer, try again\n')
            
            if game_end and not(draw):
                if self.player.get_hand_value() > 21 or (self.player.get_hand_value() < self.bank.get_hand_value() and self.bank.get_hand_value() <= 21):
                    print('\nYou lost!')

                    self.player.life -= 10
                    print(self.player.player_status())
                    print('')

                elif self.bank.get_hand_value() > 21 or (self.bank.get_hand_value() < self.player.get_hand_value() and self.player.get_hand_value() <= 21):
                    print('\nThe bank lost to you!')

                    if self.player.life < 100:
                        self.player.life += 5
                
                    print(self.player.player_status())
                    print('')

                # Checking if the player wants to continue
                while not(valid):
                    p_continue = input('Would you like to keep playing [y]/[n]: ')
                
                    match p_continue.lower():
                        case 'y':
                            game_end = 0
                            valid = 1
                        case 'n':
                            game_end = 1
                            valid = 1
                        case _:
                            print('\nNot a valid answer!\n')
                
                os.system('cls')
                valid = 0

            elif game_end and draw:
                print('\nDraw!')
                
                print(self.player.player_status())
                print('')

                # Checking if the player wants to continue
                while not(valid):
                    p_continue = input('Would you like to keep playing [y]/[n]: ')
                
                    match p_continue.lower():
                        case 'y':
                            game_end = 0
                            valid = 1
                        case 'n':
                            game_end = 1
                            valid = 1
                        case _:
                            print('\nNot a valid answer!\n')

                os.system('cls')
                valid = 0
                
            draw = 0

        if self.get_cards_quantity() < 5 and p_continue == 's':
            print(f'You doesnt have enough cards to play! {self.get_cards_quantity()} cards only')

        self.decks = None
            