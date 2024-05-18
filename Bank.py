from Hand import *


class Bank(Hand):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Bank'

    
    def __str__(self) -> str:
        string = f'BANK HAND: \n'
        string += f'{Hand.__str__(self)}'

        return string