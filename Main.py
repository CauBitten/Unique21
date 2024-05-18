from Classes.Player import *
from Classes.Bank import *
from Classes.Deck import *
from Classes.Game import *
import time
import os


# Clean terminal
os.system('cls')

decks_quantity = int(input('How many decks would you want: '))
decks = []

for i in range(0, decks_quantity):
    deck = Deck(i)
    decks.append(deck)

# Clean terminal
os.system('cls')

loading = 1
i = 1
while loading < 16:
    print('Getting everything ready' + '.' * i)
    time.sleep(0.1)

    # Clean terminal
    os.system('cls')

    i += 1
    loading += 1

    if i == 4:
        i = 1


# Clean terminal
os.system('cls')

p = Player('Cauã')
b = Bank()

game = Game(decks, p, b)
game.the_game()
