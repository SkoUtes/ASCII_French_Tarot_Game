#!/usr/plocal/bin/python3
import sys
sys.path.insert(0, './bin')
import itertools
import os
from tarotCards import *
from returnCards import *
from reading import *

#############################################################################################
#############################################################################################
os.system('cls' if os.name == 'nt' else 'clear')

print("""
.------.    ___           _   _    _____               _     .------. 
|8.--. |   / _ \         (_) (_)  |_   _|             | |    |7.--. |
| :/\: |  / /_\ \___  ___ _   _     | | __ _ _ __ ___ | |_   | :(): |
| :\/: |  |  _  / __|/ __| | | |    | |/ _` | '__/ _ \| __|  | ()() |
| '--'8|  | | | \__ \ (__| | | |    | | (_| | | | (_) | |_   | '--'7|
'------'  \_| |_/___/\___|_| |_|    \_/\__,_|_|  \___/ \__|  '------'

By: Pierce Jorgensen
Thanks to: T. Lebohec & github.com/lawreka


cards - prints all ascii artwork
exit - exit the program
playtarot - starts a game of French Tarot for two players
reading - gives a reading of 3 cards from a total of 22
info - provides some background information on tarot cards, French Tarot, and this project
help - displays a list of commands
clear - return to main menu

""")

#############################################################################################
#############################################################################################

def side_by_side(strings, size=700, space=4):
    strings = list(strings)
    result = []

    while any(strings):
        line = []

        for i, s in enumerate(strings):
            line.append(s[:size].ljust(size))
            strings[i] = s[size:]

        result.append((" " * space).join(line))

    return "\n".join(result)

#############################################################################################
#############################################################################################
while True :
    command = input("Please enter a command: ")

    if command == 'cards':
        if __name__ == "__main__":
            strings = Fool.display, Magician.display, Priestess.display, Empress.display, Emperor.display
            print(side_by_side(strings, size=21, space=2))

        if __name__ == "__main__":
            strings = Strength.display, Hermit.display, Wheel.display, Justice.display, Hanged.display
            print(side_by_side(strings, size=21, space=2))

        if __name__ == "__main__":
            strings = Death.display, Temperance.display, Devil.display, Tower.display, Star.display
            print(side_by_side(strings, size=21, space=2))

        if __name__ == "__main__":
            strings = Moon.display, Sun.display, Judgement.display, World.display
            print(side_by_side(strings, size=21, space=2))
    elif command == 'exit':
        print("...exiting")
        exit()
    elif command == 'help':
        print("""
cards - prints all ascii artwork
exit - exit the program
playtarot - starts a game of French Tarot for two players
reading - gives a reading of 3 cards from a total of 22
info - provides some background information on tarot cards, French Tarot, and this project
help - displays a list of commands
        """)
    elif command == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
.------.    ___           _   _    _____               _     .------. 
|8.--. |   / _ \         (_) (_)  |_   _|             | |    |7.--. |
| :/\: |  / /_\ \___  ___ _   _     | | __ _ _ __ ___ | |_   | :(): |
| :\/: |  |  _  / __|/ __| | | |    | |/ _` | '__/ _ \| __|  | ()() |
| '--'8|  | | | \__ \ (__| | | |    | | (_| | | | (_) | |_   | '--'7|
'------'  \_| |_/___/\___|_| |_|    \_/\__,_|_|  \___/ \__|  '------'

By: Pierce Jorgensen
Thanks to: T. Lebohec & github.com/lawreka


cards - prints all ascii artwork
exit - exit the program
playtarot - starts a game of French Tarot for two players
reading - gives a reading of 3 cards from a total of 22
info - provides some background information on tarot cards, French Tarot, and this project
help - displays a list of commands
clear - return to main menu

        """)
    elif command == 'reading':
        os.system('cls' if os.name == 'nt' else 'clear')
        reading()
        break
    elif command == 'playtarot':
        os.system('python3 ./bin/frenchTarot.py')
    elif command == 'info':
        print("""
This program was designed by Pierce Jorgensen as a final project for a coding class 
at the University of Utah. Credit for the ASCII artwork goes to K. Lawrence at
https://github.com/lawreka/ascii-tarot

The Tarot, also known as 'trionfi', 'tarocchi', or 'tarock' is a set of playing
cards invented in 15th century Europe for games such as Tarocchini, French
Tarot, and Königrufen. Since then Tarot has earned a reputation mostly for
its use in divination practices and card reading, but these games are still
played today. A tarot deck has 78 total cards unlike the traditional deck of
playing cards which contains 52.

French Tarot is played with 3 to 5 players, but typically with 4 in
competitions. It uses a deck of 78 cards with 22 trump cards that are different
from the most recognized Italian versions, as well as suited cards of Hearts, Clubs,
Spades, and Diamonds. Tarot was introduced into France in the 16th century due
to the First and Second Italian Wars, and by 1622 it surpassed even Chess in
popularity.

Divination or 'Tarot Reading' is a method of fortune-telling that is believed
to have originated some time during the 18th century. There is some controversy
concerning the initial purpose of this, but it is likely that people actually 
believed they could gain some idea of their future from this practice. While 
some practitioners today still believe in its attributed mystical properties,
others insist that it is merely a tool for self-understanding and advisement.
Nonetheless it remains a widespread practice in the world today, surpassing
interest even the games for which the cards were originally created.
        """)
    else:
        print("I'm sorry I didn't quite catch that, please enter again: ")

