# This will check for pairs from the hero's hole card and board and rank them against villian.

import dealer
import random

deck_of_cards = []
heros_hand = []
villians_hand = []
community_cards = []

dealer.deck_builder(deck_of_cards)
dealer.deal(2,deck_of_cards,heros_hand)
print(len(deck_of_cards))
dealer.deal(2,deck_of_cards,villians_hand)
dealer.deal(5,deck_of_cards,community_cards)
print("Hero's Hand:", heros_hand, "\n",
      "Villian's Hand:", villians_hand, "\n",
      "Community Cards:", community_cards)
print(len(deck_of_cards))

def quads_sets_pairs_check(hero, villian, community):
    # this checks hole and board cards for matches
    hero_pair = []
    villian_pair = []
    for card in hero:
        for community_card in community:
            if card[0] == community_card[0]:
                if card not in hero_pair:
                    hero_pair.append(card)
                if community_card not in hero_pair:
                    hero_pair.append(community_card)
    for card in villian:
        for community_card in community:
            if card[0] == community_card[0]:
                if card not in villian_pair:
                    villian_pair.append(card)
                if community_card not in villian_pair:
                    villian_pair.append(community_card)
    print(hero_pair,"\n", villian_pair)
    return hero_pair,villian_pair

def quads_sets_pairs_ranking(heros_quads_sets_pairs,
                             villians_quads_sets_pairs):
    # this will rank the quads,sets and pairs.
    if len(heros_quads_sets_pairs) == 4:
        #for card in heros_quads_sets_pairs:

        print("Hero has two pair or quads")
    if len(villians_quads_sets_pairs) == 4:
        print("Villian has two pair or quads")
    if len(heros_quads_sets_pairs) == 3:
        print("Hero has a set")
    if len(villians_quads_sets_pairs) == 3:
        print("Villian has a set")
    if heros_quads_sets_pairs == []:
        print("Hero has nothing")
    if villians_quads_sets_pairs == []:
        print("Villian has nothing")
    if len(heros_quads_sets_pairs)  == 2:
        print("hero has a pair")
    if len(villians_quads_sets_pairs) == 2:
        print("Villian has a pair")

def quads_or_two_pair_check(hand_to_check):
    # this will check if the list is quads or two pair. return true for quads, false for two pair
    count = 0
    for card in hand_to_check:
        if card[0] == hand_to_check[0][0]:
            count +=1
    if count == 4:
        print("True")
        return True
    else:
        print("False")
        return False

test_hero = [[7,"Hearts"],[7,"Clubs"]]
test_villian = [[8,"Clubs"],[10,"Spades"]]
test_community = [[3, 'Clubs'], [8, 'Spades'], [6, 'Diamonds'], [8, 'Hearts'], [7, 'Spades']]

hero_madehand, villian_madehand = quads_sets_pairs_check(heros_hand, villians_hand, community_cards)

quads_sets_pairs_ranking(hero_madehand,villian_madehand)

quads_or_two_pair_check([[10, 'Diamonds'], [10, 'Spades'], [11, 'Spades'], [11, 'Diamonds']])

#quads_sets_pairs_check(test_hero, test_villian, test_community)

