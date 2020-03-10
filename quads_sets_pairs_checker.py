# This will check for pairs,sets and full house from the hero's hole card.
# TODO finish sets_pair_quads_sorter function to differentiate between diffent combos of cards

def quads_sets_pairs_check(hole_cards, community):
    # this checks hole and board cards for matches, return a list of matches and then returning leftovers
    sets_pairs_list = []
    left_overs = []
    merged_cards = (hole_cards + community)

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
    print(sets_pairs_list)
    left_overs = sorted(left_overs, reverse=True)
    print(left_overs)
    return sets_pairs_list, left_overs


def sets_pair_quads_sorter(set_pairs_list, left_over_list):
    # this takes all possible combos of multiple cards within seven and parses them down to a hand ranking and five cards
    if len(set_pairs_list) == 7:
        # this can only be two options - quads + set, or, set + two pair. So below will figure out which.
        list_1 = []
        list_2 = []
        list_3 = []
        for card in set_pairs_list:
            if list_1 == []:
                list_1.append(card)
                continue
            if card[0] == list_1[0][0]:
                list_1.append(card)
                continue
            else:
                if list_2 == []:
                    list_2.append(card)
                    continue
                if card[0] == list_2[0][0]:
                    list_2.append(card)
                    continue
                else:
                    if list_3 == []:
                        list_3.append(card)
                        continue
                    if card[0] == list_3[0][0]:
                        list_3.append(card)
                        continue
        print("list 1", list_1)
        print("list 2", list_2)
        print("list 3", list_3)

        if list_3 == []:
            # quads + set
            first_card = set_pairs_list[0]
            card_list1 = []
            card_list2 = []
            card_list1.append(first_card)
            for card in set_pairs_list:
                if card[0] == first_card[0]:
                    if card not in card_list1:
                        card_list1.append(card)
                else:
                    card_list2.append(card)
            print(card_list1, "CardList1")
            print(card_list2, "cardlist2")
            if len(card_list1) == 4:
                card_list2.pop()
                card_list2.pop()
                quad_hand = (card_list1 + card_list2)
            else:
                card_list1.pop()
                card_list1.pop()
                quad_hand = (card_list2 + card_list1)

            return quad_hand, "Quads"
        else:
            pass
            # set + two pair should return full house with set and highest pair

    """if len(set_pairs_list) == 6:
        # quads + pair
        # set + set
        # pair x 3
    if len(set_pairs_list) == 5:
        # set + pair
    if len(set_pairs_list) == 4:
        # quads
        # pair x 2
    if len(set_pairs_list) == 3:
        # set
    if len(set_pairs_list) == 2:
        # pair
"""


test_hero = [[7, "Hearts"], [8, "Clubs"]]
test_villian = [[12, "Clubs"], [13, "Spades"]]
test_community = [[8, 'Spades'], [7, 'Spades'], [7, 'Diamonds'], [8, 'Diamonds'], [7, 'Clubs']]
test_var1_sets_etc, test_var2_left_overs = quads_sets_pairs_check(test_hero, test_community)
print(test_var1_sets_etc)
print(test_var2_left_overs)
print(sets_pair_quads_sorter(test_var1_sets_etc, test_var2_left_overs))

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
