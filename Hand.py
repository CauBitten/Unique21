from Card import *


class Hand:
    def __init__(self) -> None:
        self.cards = []
        self.hand_value = 0
        self.as_mutation = 0


    def __str__(self) -> str:
        string = ''

        count = 0
        for card in self.cards:
            string += f'[{card.suit} | {card.value}] '

            count += 1
            if count % 5 == 0:
                string += '\n'
        
        string += f':: {self.hand_value}'
        
        return string
    

    def get_hand_value(self) -> int:
        return self.hand_value
    

    def add_card(self, card) -> None:
        self.cards.append(card)

        match card.value:
                case 'A':
                    self.hand_value += 11

                case 'J':
                    self.hand_value += 10

                case 'Q':
                    self.hand_value += 10

                case 'K':
                    self.hand_value += 10
                
                case _:
                    value = int(card.value)
                    self.hand_value += value

        self.upload_points()

    
    def upload_points(self):
        as_quantity = self.set_as_quantity()

        for card in self.cards:
            if card.value == 'A' and self.hand_value > 21 and self.as_mutation < as_quantity:
                self.hand_value -= 10
                self.as_mutation += 1


    def set_as_quantity(self) -> int:
        as_quantity = 0

        for card in self.cards:
            if card.value == 'A':
                as_quantity += 1
        
        return as_quantity


    def clear_hand(self):
        self.cards = []
        self.hand_value = 0
        self.as_mutation = 0