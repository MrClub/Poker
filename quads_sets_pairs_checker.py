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

test_hero = [[7,"Hearts"],[7,"Clubs"]]
test_villian = [[8,"Clubs"],[10,"Spades"]]
test_community = [[3, 'Clubs'], [8, 'Spades'], [6, 'Diamonds'], [8, 'Hearts'], [7, 'Spades']]

quads_sets_pairs_check(heros_hand, villians_hand, community_cards)

#quads_sets_pairs_check(test_hero, test_villian, test_community)

