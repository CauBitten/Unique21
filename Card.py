class Card:
    def __init__(self, suit:chr, value:chr) -> None:
        self.suit = suit
        self.value = value


    def __str__(self):
        return f'{self.suit} | {self.value}'


    def get_suit(self):
        return self.suit
    
    
    def get_value(self):
        return self.value
    