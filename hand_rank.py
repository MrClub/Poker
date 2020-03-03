# This will rank each hand. It will pull all the individual checks ie flush_check, straight_check into a
# coherent whole

import flush_check as flush
import straight_check as straight

# TODO need to rewrite quads_sets_pairs_checker. To return true or false based on hand
# TODO highest_card_rank needs to be rewritten to return True/False. Or does it? It's just a compare function..
#

test_hero = [[7,"Hearts"],[2,"Clubs"]]
test_villian = [[8,"Hearts"],[10,"Hearts"]]
test_community = [[3, 'Clubs'], [8, 'Spades'], [9, 'Hearts'], [6, 'Hearts'], [10, 'Hearts']]

def hand_rank(hole_cards, community_cards):
    # Will pull all individual hand rank checks together.
    if flush.flush_check(hole_cards,community_cards):
        print("Flush")
        print(flush.flush_check(hole_cards,community_cards))
    elif straight.straight_check(hole_cards,community_cards):
        print("Straight")
        print(straight.straight_check(hole_cards,community_cards))

hand_rank(test_hero,test_community)

