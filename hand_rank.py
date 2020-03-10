# This will rank each hand. It will pull all the individual checks ie flush_check, straight_check into a
# coherent whole

import straight_flush_check as sfc

# TODO highest_card_rank needs to be rewritten to return True/False. Or does it? It's just a compare function..
#

test_hero = [[13,"Hearts"],[12,"Hearts"]]
test_villian = [[8,"Hearts"],[10,"Hearts"]]
test_community = [[3, 'Clubs'], [8, 'Spades'], [14, 'Hearts'], [11, 'Hearts'], [10, 'Hearts']]

def hand_rank(hole_cards, community_cards):
    # Will pull all individual hand rank checks together.

    if sfc.straight_flush_check(hole_cards,community_cards):
        print(sfc.straight_flush_check(hole_cards,community_cards))

hand_rank(test_hero,test_community)

