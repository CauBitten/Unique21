import numpy as np
from Card import *


suits = ['P', 'O', 'C', 'E']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    def __init__(self, id) -> None:
        self.deck = []
        self.id = id

        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))


    def __str__(self) -> str:
        string = 'DECK: \n\n'

        count = 0
        for card in self.deck:
            string += f'[{card.suit} | {card.value}] '

            count += 1
            if count % 13 == 0:
                string += '\n'

        return string


    def get_deck(self) -> list:
        return self.deck
    

    def get_deck_len(self) -> int:
        return len(self.deck)


    def get_card_from_deck(self) -> Card:
        size = self.get_deck_len()

        index = np.random.randint(0, size-1)
        
        card = self.deck[index]
        del(self.deck[index])

        if len(self.deck) == 0:
            self.deck = None

        return card
    

    def delete_card_from_deck(self, index):
        del(self.deck[index])