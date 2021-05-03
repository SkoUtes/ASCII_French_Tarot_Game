#!/usr/plocal/bin/python3
import random as random
import returnCards
from returnCards import *
import itertools
import os
import time

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
deck = [ spade1, spade2, spade3, spade4, spade5, spade6, spade7, spade8, spade9, spade10, spadeJ, spadeC, spadeQ, spadeK, diamond1, diamond2, diamond3, diamond4, diamond5, diamond6, diamond7, diamond8, diamond9, diamond10, diamondJ, diamondC, diamondQ, diamondK, heart1, heart2, heart3, heart4, heart5, heart6, heart7, heart8, heart9, heart10, heartJ, heartC, heartQ, heartK, club1, club2, club3, club4, club5, club6, club7, club8, club9, club10, clubJ, clubC, clubQ, clubK, Fool, Magician, Priestess, Empress, Emperor, Hierophant, Lovers, Chariot, Strength, Hermit, Wheel, Justice, Hanged, Death, Temperance, Devil, Tower, Star, Moon, Sun, Judgement, World ]

deck_strings = [ "1spades", "2spades", "3spades", "4spades", "5spades", "6spades", "7spades", "8spades", "9spades", "10spades", "Jspades", "Cspades", "Qspades", "Kspades", "1diamonds", "2diamonds", "3diamonds", "4diamonds", "5diamonds", "6diamonds", "7diamonds", "8diamonds", "9diamonds", "10diamonds", "Jdiamonds", "Cdiamonds", "Qdiamonds", "Kdiamonds", "1hearts", "2hearts", "3hearts", "4hearts", "5hearts", "6hearts", "7hearts", "8hearts", "9hearts", "10hearts", "Jhearts", "Chearts", "Qhearts", "Khearts", "1clubs", "2clubs", "3clubs", "4clubs", "5clubs", "6clubs", "7clubs", "8clubs", "9clubs", "10clubs", "Jclubs", "Cclubs", "Qclubs", "Kclubs", "fool-0", "magician-1", "priestess-2", "empress-3", "emperor-4", "hierophant-5", "lovers-6", "chariot-7", "strength-8", "hermit-9", "wheel-10", "justice-11", "hanged-12", "death-13", "temperance-14", "devil-15", "tower-16", "star-17", "moon-18", "sun-19", "judgement-20", "world-21" ]

#############################################################################################
random.shuffle(deck) # Shuffle the cards
p1hand = []
p1pile = []

p2hand = []
p2pile = []
#############################################################################################
for line in itertools.islice(deck, 0, 21):
    p1hand.append(line)
for line in itertools.islice(deck, 42, 60):
    p1pile.append(line)
#############################################################################################
for line in itertools.islice(deck, 21, 42):
    p2hand.append(line)
for line in itertools.islice(deck, 60, 78):
    p2pile.append(line)
#############################################################################################
p1score = []
p2score = []

############################ Define the game's turn system ##################################
#############################################################################################
# This section defines 8 turns for 2 tricks. 1 trick where player 1 starts, and
# 1 trick where player 2 starts.

def trick():
    os.system('cls' if os.name == 'nt' else 'clear')
    played = []
    showp1 = []
    for i in p1pile[::3]:
        showp1.append(i.display)
    if __name__ == "__main__":
        strings = showp1
        print(side_by_side(strings, size=21, space=2))
    print("Your pile contains the cards: ")
    for i in p1pile[::3]:
        print(i.name, end=", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p1hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            print("Oops, you can't forfeit on the first turn of a trick.")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp1
                print(side_by_side(strings, size=21, space=2))
            print("Your pile contains the cards: ")
            for i in p1pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p1hand, p1pile[::3]):
                if varname == a.name:
                    played.append(a)
                    check = 1
                    p1hand.remove(a)
                    win = "player1"
                    break
                elif varname == b.name:
                    played.append(b)
                    check = 1
                    p1pile.remove(b)
                    win = "player1"
                    break
                else:
                    pass
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    cardsplayed = []
    for i in played:
        cardsplayed.append(i.name)
    print("")
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    contin = input("Pass the keyboard off to player 2. Player 2, press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
#############################################################################################
    showp2 = []
    for i in p2pile[::3]:
        showp2.append(i.display)
    if __name__ == "__main__":
        strings = showp2
        print(side_by_side(strings, size=21, space=2))
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    print("Your pile contains these cards: ")
    for i in p2pile[::3]:
        print(i.name, end = ", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p2hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            fcard = input("Select a card to forfeit: ")
            if fcard in deck_strings:
                for a,b in zip(p2hand, p2pile[::3]):
                    if fcard == a.name:
                        played.append(a)
                        p2hand.remove(a)
                        win = "player1"
                        check = 1
                    elif fcard == b.name:
                        played.append(b)
                        p2pile.remove(b)
                        win = "player1"
                        check = 1
            else:
                print("Oops, I think you may have misspelled. Type forfeit to try again")
                print("")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp2
                print(side_by_side(strings, size=21, space=2))
            print("The last cards played were: ", cardsplayed)
            print("The current suit is:", played[-1].suit)
            print("")
            print("Your pile contains the cards: ")
            for i in p2pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p2hand, p2pile[::3]):
                if varname == a.name:
                    print(a.name)
                    if a.suit == currentsuit and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p2hand.remove(a)
                        win = "player2"
                        break
                    elif a.suit == "trump" and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p2hand.remove(a)
                        win = "player2"
                        break
                elif varname == b.name:
                    print(b.name)
                    if b.suit == currentsuit and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p2pile.remove(b)
                        win = "player2"
                        break
                    elif b.suit == "trump" and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p2pile.remove(b)
                        win = "player2"
                        break
        elif varname == "skip":
            check = 1
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
            pass
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    cardsplayed.clear()
    for i in played:
        cardsplayed.append(i.name)
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    contin = input("Pass the keyboard off to player 1. Player 1, press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
#############################################################################################
    showp1 = []
    for i in p1pile[::3]:
        showp1.append(i.display)
    if __name__ == "__main__":
        strings = showp1
        print(side_by_side(strings, size=21, space=2))
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    print("Your pile contains these cards: ")
    for i in p1pile[::3]:
        print(i.name, end = ", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p1hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            fcard = input("Select a card to forfeit: ")
            if fcard in deck_strings:
                for a,b in zip(p1hand, p1pile[::3]):
                    if fcard == a.name:
                        played.append(a)
                        p1hand.remove(a)
                        win = "player2"
                        check = 1
                    elif fcard == b.name:
                        played.append(b)
                        p1pile.remove(b)
                        win = "player2"
                        check = 1
            else:
                print("Oops, I think you may have misspelled. Type forfeit to try again")
                print("")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp1
                print(side_by_side(strings, size=21, space=2))
            print("The last cards played were: ", cardsplayed)
            print("The current suit is:", played[-1].suit)
            print("")
            print("Your pile contains the cards: ")
            for i in p1pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p1hand, p1pile[::3]):
                if varname == a.name:
                    print(a.name)
                    if a.suit == currentsuit and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p1hand.remove(a)
                        win = "player1"
                        break
                    elif a.suit == "trump" and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p1hand.remove(a)
                        win = "player1"
                        break
                elif varname == b.name:
                    print(b.name)
                    if b.suit == currentsuit and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p1pile.remove(b)
                        win = "player1"
                        break
                    elif b.suit == "trump" and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p1pile.remove(b)
                        win = "player1"
                        break
        elif varname == "skip":
            check = 1
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
            pass
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    cardsplayed.clear()
    for i in played:
        cardsplayed.append(i.name)
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    contin = input("Pass the keyboard off to player 2. Player 2, press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
#############################################################################################
    showp2 = []
    for i in p2pile[::3]:
        showp2.append(i.display)
    if __name__ == "__main__":
        strings = showp2
        print(side_by_side(strings, size=21, space=2))
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    print("Your pile contains these cards: ")
    for i in p2pile[::3]:
        print(i.name, end = ", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p2hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            fcard = input("Select a card to forfeit: ")
            if fcard in deck_strings:
                for a,b in zip(p2hand, p2pile[::3]):
                    if fcard == a.name:
                        played.append(a)
                        p2hand.remove(a)
                        win = "player1"
                        check = 1
                    elif fcard == b.name:
                        played.append(b)
                        p2pile.remove(b)
                        win = "player1"
                        check = 1
            else:
                print("Oops, I think you may have misspelled. Type forfeit to try again")
                print("")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp2
                print(side_by_side(strings, size=21, space=2))
            print("The last cards played were: ", cardsplayed)
            print("The current suit is:", played[-1].suit)
            print("")
            print("Your pile contains the cards: ")
            for i in p2pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p2hand, p2pile[::3]):
                if varname == a.name:
                    print(a.name)
                    if a.suit == currentsuit and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p2hand.remove(a)
                        win = "player2"
                        break
                    elif a.suit == "trump" and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p2hand.remove(a)
                        win = "player2"
                        break
                elif varname == b.name:
                    print(b.name)
                    if b.suit == currentsuit and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p2pile.remove(b)
                        win = "player2"
                        break
                    elif b.suit == "trump" and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p2pile.remove(b)
                        win = "player2"
                        break
        elif varname == "skip":
            check = 1
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
            pass
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    cardsplayed.clear()
    for i in played:
        cardsplayed.append(i.name)
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    if win == "player1":
        for i in played:
            p1score.append(i.value)
        print("Player 1 wins the trick with plus", sum(p1score), "points!")
        input("Player 1 will start next. Press enter to continue: ")
        played.clear()
        if sum(p1score) > 26 and sum(p1score) > sum(p2score):
            return
    if win == "player2":
        for i in played:
            p2score.append(i.value)
        print("Player 2 wins the trick with plus", sum(p2score), "points!")
        input("Player 2 will start next. Press enter to continue: ")
        played.clear()
        if sum(p2score) > 26 and sum(p2score) > sum(p1score):
            return
    os.system('cls' if os.name == 'nt' else 'clear')
######################################### Trick 2 ###########################################
#########################################  Begin  ###########################################
    showp2 = []
    for i in p2pile[::3]:
        showp2.append(i.display)
    if __name__ == "__main__":
        strings = showp1
        print(side_by_side(strings, size=21, space=2))
    print("Your pile contains the cards: ")
    for i in p2pile[::3]:
        print(i.name, end=", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p2hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            print("Oops, you can't forfeit on the first turn of a trick.")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp2
                print(side_by_side(strings, size=21, space=2))
            print("Your pile contains the cards: ")
            for i in p2pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p2hand, p2pile[::3]):
                if varname == a.name:
                    played.append(a)
                    check = 1
                    p2hand.remove(a)
                    win = "player2"
                    break
                elif varname == b.name:
                    played.append(b)
                    check = 1
                    p2pile.remove(b)
                    win = "player2"
                    break
                else:
                    pass
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    cardsplayed = []
    for i in played:
        cardsplayed.append(i.name)
    print("")
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    contin = input("Pass the keyboard off to player 1. Player 1, press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
#############################################################################################
    showp1 = []
    for i in p1pile[::3]:
        showp1.append(i.display)
    if __name__ == "__main__":
        strings = showp1
        print(side_by_side(strings, size=21, space=2))
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    print("Your pile contains these cards: ")
    for i in p1pile[::3]:
        print(i.name, end = ", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p1hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            fcard = input("Select a card to forfeit: ")
            if fcard in deck_strings:
                for a,b in zip(p1hand, p1pile[::3]):
                    if fcard == a.name:
                        played.append(a)
                        p1hand.remove(a)
                        win = "player2"
                        check = 1
                    elif fcard == b.name:
                        played.append(b)
                        p1pile.remove(b)
                        trackwin = 1
                        win = "player2"
                        check = 1
            else:
                print("Oops, I think you may have misspelled. Type forfeit to try again")
                print("")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp1
                print(side_by_side(strings, size=21, space=2))
            print("The last cards played were: ", cardsplayed)
            print("The current suit is:", played[-1].suit)
            print("")
            print("Your pile contains the cards: ")
            for i in p1pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p1hand, p1pile[::3]):
                if varname == a.name:
                    print(a.name)
                    if a.suit == currentsuit and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p1hand.remove(a)
                        win = "player1"
                        break
                    elif a.suit == "trump" and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p1hand.remove(a)
                        win = "player1"
                        break
                elif varname == b.name:
                    print(b.name)
                    if b.suit == currentsuit and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p1pile.remove(b)
                        win = "player1"
                        break
                    elif b.suit == "trump" and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p1pile.remove(b)
                        win = "player1"
                        break
        elif varname == "skip":
            check = 1
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
            pass
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    cardsplayed.clear()
    for i in played:
        cardsplayed.append(i.name)
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    contin = input("Pass the keyboard off to player 2. Player 2, press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
#############################################################################################
    showp2 = []
    for i in p2pile[::3]:
        showp2.append(i.display)
    if __name__ == "__main__":
        strings = showp2
        print(side_by_side(strings, size=21, space=2))
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    print("Your pile contains these cards: ")
    for i in p2pile[::3]:
        print(i.name, end = ", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p2hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            fcard = input("Select a card to forfeit: ")
            if fcard in deck_strings:
                for a,b in zip(p2hand, p2pile[::3]):
                    if fcard == a.name:
                        played.append(a)
                        p2hand.remove(a)
                        win = "player1"
                        check = 1
                    elif fcard == b.name:
                        played.append(b)
                        p2pile.remove(b)
                        win = "player1"
                        check = 1
            else:
                print("Oops, I think you may have misspelled. Type forfeit to try again")
                print("")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp2
                print(side_by_side(strings, size=21, space=2))
            print("The last cards played were: ", cardsplayed)
            print("The current suit is:", played[-1].suit)
            print("")
            print("Your pile contains the cards: ")
            for i in p2pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p2hand:
                print(i.name, end=", ")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p2hand, p2pile[::3]):
                if varname == a.name:
                    print(a.name)
                    if a.suit == currentsuit and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p2hand.remove(a)
                        win = "player2"
                        break
                    elif a.suit == "trump" and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p2hand.remove(a)
                        win = "player2"
                        break
                elif varname == b.name:
                    print(b.name)
                    if b.suit == currentsuit and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p2pile.remove(b)
                        win = "player2"
                        break
                    elif b.suit == "trump" and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p2pile.remove(b)
                        win = "player2"
                        break
        elif varname == "skip":
            check = 1
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
            pass
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    cardsplayed.clear()
    for i in played:
        cardsplayed.append(i.name)
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    contin = input("Pass the keyboard off to player 1. Player 1, press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
#############################################################################################
    showp1 = []
    for i in p1pile[::3]:
        showp1.append(i.display)
    if __name__ == "__main__":
        strings = showp1
        print(side_by_side(strings, size=21, space=2))
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    print("Your pile contains these cards: ")
    for i in p1pile[::3]:
        print(i.name, end = ", ")
    print("")
    print("")
    print("Your hand contains the cards: ")
    for i in p1hand:
        print(i.name, end=", ")
    print("")
    print("")
    print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
    """)
    while True:
        check = 0
        varname = input("Please select an option: ")
        if varname == "hand":
            print("")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("")
        elif varname == "forfeit":
            fcard = input("Select a card to forfeit: ")
            if fcard in deck_strings:
                for a,b in zip(p1hand, p1pile[::3]):
                    if fcard == a.name:
                        played.append(a)
                        p1hand.remove(a)
                        win = "player2"
                        check = 1
                    elif fcard == b.name:
                        played.append(b)
                        p1pile.remove(b)
                        win = "player2"
                        check = 1
            else:
                print("Oops, I think you may have misspelled. Type forfeit to try again")
                print("")
        elif varname == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            if __name__ == "__main__":
                strings = showp1
                print(side_by_side(strings, size=21, space=2))
            print("The last cards played were: ", cardsplayed)
            print("The current suit is:", played[-1].suit)
            print("")
            print("Your pile contains the cards: ")
            for i in p1pile[::3]:
                print(i.name, end=", ")
            print("")
            print("")
            print("Your hand contains the cards: ")
            for i in p1hand:
                print(i.name, end=", ")
            print("")
            print("""===============================================
Type 'hand' to see your cards.
Type 'forfeit' to give up a card if you can't play anything.
To play a card, type the card name exactly as displayed.
Type 'clear' to get the default screen again.
Type 'skip' if the game is breaking :c
===============================================
            """)
        elif varname in deck_strings:
            for a,b in zip(p1hand, p1pile[::3]):
                if varname == a.name:
                    print(a.name)
                    if a.suit == currentsuit and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p1hand.remove(a)
                        win = "player1"
                        break
                    elif a.suit == "trump" and a.priority > currentpriority:
                        played.append(a)
                        check = 1
                        p1hand.remove(a)
                        win = "player1"
                        break
                elif varname == b.name:
                    print(b.name)
                    if b.suit == currentsuit and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p1pile.remove(b)
                        win = "player1"
                        break
                    elif b.suit == "trump" and b.priority > currentpriority:
                        played.append(b)
                        check = 1
                        p1pile.remove(b)
                        win = "player1"
                        break
        elif varname == "skip":
            check = 1
        else:
            check = 2
        if check == 0:
            pass
        elif check == 1:
            break
        elif check == 2:
            print("Oops, I didn't quite catch that. Make sure you enter the card name exactly as displayed.")
            pass
#############################################################################################
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    cardsplayed.clear()
    for i in played:
        cardsplayed.append(i.name)
    print("The last cards played were: ", cardsplayed)
    print("The current suit is:", played[-1].suit)
    print("")
    currentsuit = played[-1].suit
    currentpriority = played[-1].priority
    if win == "player1":
        for i in played:
            p1score.append(i.value)
        print("Player 1 wins the trick with a new total of", sum(p1score), "points!")
        input("Player 1 will start next. Press enter to continue: ")
        played.clear()
    if win == "player2":
        for i in played:
            p2score.append(i.value)
        print("Player 2 wins the trick with a new total of", sum(p2score), "points!")
        input("Player 2 will start next. Press enter to continue: ")
        played.clear()
    os.system('cls' if os.name == 'nt' else 'clear')
#############################################################################################
#############################################################################################

def game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    How to play:

    The deck consits of 78 cards with five suits.

    The standard suited cards are numbered Ace-10, each with a Roi, Dame, Cavalier, and Valet (King, Queen, Knight and Jack). The value of cards is
    in order of Ace as the lowest card (1) to King as the highest (14).

    The trump suit consists of 22 cards numbered 0-21. All trump cards beat suited cards, but higher trump cards beat lower ones (ie Chariot beats Fool). 
    To clarify this, all trump cards have a number next to their name. Three of the trump cards are called 'Bouts' which are worth extra points at
    the end of the game. The three Bouts are the Fool, the Magician, and the World.

    The point values of the cards are counted up at the end as follows:
    Bouts (0,1,21): 4.5 points
    Kings:          4.5 points
    Queens:         3.5 points
    Knights:        2.5 points
    Jacks:          1.5 points
    Pip cards:      0.5 points
    Trumps:         0.5 points

    The goal of the game is to win 'tricks' by playing one of 6 or fewer available cards from a pile in front of you, or playing cards in your hand.
    The player who puts down the highest value card will win the trick. Keep in mind normal trump cards are only worth 0.5 points each. 
    In this version of the game, a trick is 4 turns (2 for each player). The first to 26 points and no tie wins.

    The starting player will place a card of any suit, and then the opposing player must play a card of that suit of higher value. If no cards can be
    played, then you must forfeit a card. The player who wins the trick gets to add the cards played to their total score.

    Note: Many historical and linguistic liberties were taken with this game to adapt it to this program. Normally the game is not played with two people,
    has all card names in French, and bets/other rules have been omitted.

    Known Issues: There are some major flaws with the game as it stands. If you play a card that's not high enough or of the wrong suit. The game will
    break and you have to skip your turn. In addition, sometimes the game will break for no reason at all and it may work if you pick a card from the pile 
    instead, but otherwise you must skip. After spending much time trying to discern this issue it seems to be part of the way for-loops
    run and are seen by the interpreter. There seems to be no way to fix this without a major redesign of the program.
    """)
    input("If you are ready to play press Enter to start the game: ")
    while True:
        trick()
        if sum(p1score) > 26 and sum(p1score) > sum(p2score):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("Game over, Player 1 wins with a score of ", sum(p1score), "! Thanks for playing :D", sep="")
            break
        if sum(p2score) > 26 and sum(p2score) > sum(p1score):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("Game over, Player 2 wins with a score of ", sum(p2score), "! Thanks for playing :D", sep="")
            break

game()
            


