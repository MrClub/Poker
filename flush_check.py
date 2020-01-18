# This will check for flushes

import dealer
import random
deck_of_cards = []
hero_hole = []
villian_hole = []
community_cards =[]

dealer.deck_builder(deck_of_cards)
dealer.deal(2,deck_of_cards,hero_hole)
dealer.deal(2,deck_of_cards,villian_hole)
dealer.deal(5,deck_of_cards,community_cards)

def flush_check(hole_cards,community_cards):
    diamonds = 0
    hearts = 0
    spades = 0
    clubs = 0
    for card in hole_cards:
        if card[1] == "Diamonds":
            diamonds += 1
        elif card[1] == "Hearts":
            hearts +=1
        elif card[1] == "Spades":
            spades += 1
        else:
            clubs +=1
    for card in community_cards:
        if card[1] == "Diamonds":
            diamonds += 1
        elif card[1] == "Hearts":
            hearts +=1
        elif card[1] == "Spades":
            spades += 1
        else:
            clubs +=1
    print(" Diamonds",diamonds,"\n",
          "Hearts",hearts,"\n",
          "Spades",spades,"\n",
          "Clubs",clubs)
    if diamonds >= 5 or hearts >= 5 or spades >= 5 or clubs >= 5:
        print("There is a flush")
        return True

flush_check(hero_hole,community_cards)
flush_check(villian_hole,community_cards)