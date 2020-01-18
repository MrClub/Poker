# this will test for straights.
# TODO: Make straight_check.py detect wheel straights i.e ace,2,3,4,5
# TODO: Write straight_check function which can tell which player has the higher straight ie straight_rank

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
    #finds best straight and returns it, else returns empty list
    merged_cards = sorted(hole_cards + community_cards)
    count = 0
    straight_number = merged_cards[0][0]
    straight_list =[]
    print(merged_cards)
    for card in merged_cards:
        if card[0] == straight_number + 1:
            count +=1
            straight_number = card[0]
            straight_list.append(card)
        else:
            if count >= 4:
                continue
                # we can't have more than 2 straights in 7 cards so it's okay to continue
            count = 0
            straight_number = card[0]
            straight_list =[card]
    print(straight_list)
    print(len(straight_list))
    # below check the straight length and trims it to the best five
    if len(straight_list) < 5:
        straight_list =[]
    if len(straight_list) == 6:
        straight_list = sorted(straight_list, reverse=True)
        straight_list.pop()
    if len(straight_list) == 7:
        straight_list = sorted(straight_list, reverse=True)
        straight_list.pop()
        straight_list.pop()
    print(straight_list)
    return straight_list



test_hole = [[2, 'Hearts'], [3, 'Hearts']]
test_community = [[4, 'Hearts'], [5, 'Hearts'], [6, 'Diamonds'], [7, 'Clubs'], [8, 'Spades'],]
#straight_check(hero_hole,community_cards)
straight_check(test_hole,test_community)