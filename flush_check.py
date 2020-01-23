# This will check for flushes
# TODO write something to rank flushes

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
    # checks for flush, if more than five cards returns best.
    diamonds = []
    hearts = []
    spades = []
    clubs = []
    merged_cards = sorted(hole_cards,community_cards)
    for card in merged_cards:
        if card[1] == "Diamonds":
            diamonds.append(card)
        elif card[1] == "Hearts":
            hearts.append(card)
        elif card[1] == "Spades":
            spades.append(card)
        else:
            clubs.append(card)

    print(" Diamonds",diamonds,"\n",
          "Hearts",hearts,"\n",
          "Spades",spades,"\n",
          "Clubs",clubs)

    if len(diamonds) >= 5:
        diamonds = sorted(diamonds,reverse=True)
        if len(diamonds) == 6 or len(diamonds) == 7:
            diamonds = flush_ranking(diamonds)
        return diamonds
    if len(hearts) >= 5:
        hearts = sorted(hearts,reverse=True)
        if len(hearts) == 6 or len(hearts) == 7:
            hearts = flush_ranking(hearts)
        return hearts
    if len(spades) >= 5:
        spades = sorted(spades,reverse=True)
        if len(spades) == 6 or len(spades) == 7:
            spades = flush_ranking(spades)
        return spades
    if len(clubs) >= 5:
        clubs = sorted(clubs,reverse=True)
        if len(clubs) == 6 or len(clubs) == 7:
            clubs = flush_ranking(clubs)
        return clubs
    return []



def flush_ranking(flush_list):
    # take a flush of 5 greater cards and trims it to best five
    if len(flush_list) ==6:
        flush_list.pop()
    if len(flush_list) == 7:
        flush_list.pop()
        flush_list.pop()
    return flush_list

flush_check(hero_hole,community_cards)
flush_check(villian_hole,community_cards)