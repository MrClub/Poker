# This will check for pairs,sets and full house from the hero's hole card.


def quads_sets_pairs_check(hole_cards, community):
    # this checks hole and board cards for matches, return a list of matches and then returning leftovers
    sets_pairs_list = []
    left_overs = []
    merged_cards = (hole_cards+community)

    for card in merged_cards:
        for item in merged_cards:
            if item == card:
                continue
            else:
                if card[0] == item[0]:
                    if card not in sets_pairs_list:
                        sets_pairs_list.append(card)
                        sets_pairs_list.append(item)
                    elif item not in sets_pairs_list:
                        sets_pairs_list.append(item)

    for card in merged_cards:
        if card not in sets_pairs_list:
            left_overs.append(card)
    sets_pairs_list = sorted(sets_pairs_list, reverse=True)
    left_overs = sorted(left_overs, reverse=True)
    return sets_pairs_list,left_overs

def sets_pair_quads_sorter(set_pairs_list,left_over_list):
    if len(set_pairs_list) == 7:
        # quads + set
        # set + two pair
    if len(set_pairs_list) == 6:
        # quads + pair
        # set + set
        # pair x 3
    if len(set_pairs_list) == 5:
        # set + pair
    if len(set_pairs_list) == 4:
        # quads
        # pair x 2
    if len(set_pairs_list) = 3:
        # set
    if len(set_pairs_list) == 2:
        # pair


test_hero = [[7,"Hearts"],[7,"Clubs"]]
test_villian = [[8,"Clubs"],[10,"Spades"]]
test_community = [[3, 'Clubs'], [8, 'Spades'], [6, 'Diamonds'], [8, 'Hearts'], [7, 'Spades']]
print(quads_sets_pairs_check(test_hero,test_community))




"""for card in hole_cards:
        # this goes through cards and looks for pairs or sets
        for community_card in community:
            if card[0] == community_card[0]:
                if card not in sets_pairs_list:
                    sets_pairs_list.append(card)
                if community_card not in sets_pairs_list:
                    sets_pairs_list.append(community_card)

for other_card in merged_cards:
        # this figures out what is not in a pair or set and puts them in a list (eg so I can figure out highest card with a quad)
        if other_card not in sets_pairs_list:
            left_overs.append(other_card)
    return sets_pairs_list, left_overs

test_hero = [[7,"Hearts"],[7,"Clubs"]]
test_villian = [[8,"Clubs"],[10,"Spades"]]
test_community = [[3, 'Clubs'], [8, 'Spades'], [6, 'Diamonds'], [8, 'Hearts'], [7, 'Spades']]
print(quads_sets_pairs_check(test_hero,test_community))

def quads_sets_pairs_ranking(heros_quads_sets_pairs,
                             villians_quads_sets_pairs):
    # this will rank the quads,sets and pairs.
    if len(heros_quads_sets_pairs) == 4:
        if quads_or_two_pair_check(heros_quads_sets_pairs):
            print("Hero has quads")
        else:
            print("Hero has two pair")


    if len(villians_quads_sets_pairs) == 4:
        if quads_or_two_pair_check(villians_quads_sets_pairs):
            print("Villian has quads")
        else:
            print("Villian has two pair")

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
test_community = [[3, 'Clubs'], [8, 'Spades'], [6, 'Diamonds'], [8, 'Hearts'], [7, 'Spades']]"""



