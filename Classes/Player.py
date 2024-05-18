from Classes.Hand import *


class Player(Hand):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.life = 100

    
    def __str__(self) -> str:
        string = '\nPLARYER HAND: \n'
        string += f'{Hand.__str__(self)}'

        return string
    

    def player_status(self) -> str:
        string = f'\nPLARYER STATUS:\n'
        string += f'Name: {self.name} | Life: {self.life}'

        return string