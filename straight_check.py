# this will test for straights.

import dealer
import random

deck_of_cards = []
hero_hole = []
villian_hole =[]
community_cards=[]


dealer.deck_builder(deck_of_cards)
dealer.deal(2,deck_of_cards,hero_hole)
dealer.deal(2,deck_of_cards,villian_hole)
dealer.deal(5,deck_of_cards,community_cards)

def straight_check(hole_cards,community_cards):
    merged_cards = sorted(hole_cards + community_cards)
    count = 0
    straight_number = merged_cards[0][0]
    print(merged_cards)
    for card in merged_cards:
        if card[0] == straight_number + 1:
            count +=1
            straight_number = card[0]
            if count == 4:
                print("This is a straight")
                continue
        else:
            count = 0
            straight_number = card[0]
    print("no straight")


straight_check(hero_hole,community_cards)