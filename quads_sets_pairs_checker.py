# This will check for pairs,sets and full house from the hero's hole card.
# TODO finish sets_pair_quads_sorter function to differentiate between diffent combos of cards
# TODO write checks if length of sorter list equals 6

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
    left_over_list = sorted(left_over_list,reverse=True)
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
    if len(set_pairs_list) == 7:
        # this can only be two options - quads + set, or, set + two pair. So below will figure out which.
        if not list_3:
            # must be quads + set
            if len(list_1) == 4:
                list_2.pop()
                list_2.pop()
                quad_hand = (list_1 + list_2)
            else:
                list_1.pop()
                list_1.pop()
                quad_hand = (list_2 + list_1)

            return quad_hand, "Quads"
        else:
            # set + two pair should return full house with set and highest pair
            if len(list_1) == 3:
                if list_2[0][0] > list_3[0][0]:
                    full_house_hand = (list_1 + list_2)
                    return full_house_hand, "Full House"
                else:
                    full_house_hand = (list_1 + list_3)
                    return full_house_hand, "Full House"
            elif len(list_2) == 3:
                if list_1[0][0] > list_3[0][0]:
                    full_house_hand = (list_2 + list_1)
                    return full_house_hand, "Full House"
                else:
                    full_house_hand = (list_2 + list_3)
                    return full_house_hand, "Full House"
            else:
                if list_1[0][0] > list_2[0][0]:
                    full_house_hand = (list_3 + list_1)
                    return full_house_hand, "Full House"
                else:
                    full_house_hand = (list_3 + list_2)
                    return full_house_hand, "Full House"

    if len(set_pairs_list) == 6:
        if not list_3:
            # quads + pair
            # set + set
            if len(list_1) == 3:
            # set + set
                if list_1[0][0] > list_2[0][0]:
                    list_2.pop()
                    full_house_hand = (list_1 + list_2)
                    return full_house_hand, "Full House"
                else:
                    list_1.pop()
                    full_house_hand = (list_2 + list_1)
                    return full_house_hand, "Full House"

            else:
                # quads + pair
                if len(list_1) == 4:
                    left_over_list = sorted(left_over_list + list_2, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    quads_hand = list_1 + left_over_list
                    return quads_hand, "Quads"
                else:
                    left_over_list = sorted(left_over_list + list_1, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    quads_hand = list_2 + left_over_list
                    return quads_hand, "Quads"
        else:
            # pair x 3
            if list_1[0][0] > list_2[0][0] and list_1[0][0] > list_3[0][0]:
                if list_2[0][0] > list_3[0][0]:
                    left_over_list = sorted(left_over_list + list_3, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    two_pair_hand = list_1 + list_2 + left_over_list
                    return two_pair_hand, "Two Pair"
                else:
                    left_over_list = sorted(left_over_list + list_2, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    two_pair_hand = list_1 + list_3 + left_over_list
                    return two_pair_hand, "Two Pair"
            elif list_2[0][0] > list_1[0][0] and list_2[0][0] > list_3[0][0]:
                if list_1[0][0] > list_3[0][0]:
                    left_over_list = sorted(left_over_list + list_3, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    two_pair_hand = list_2 + list_1 + left_over_list
                    return two_pair_hand, "Two Pair"
                else:
                    left_over_list = sorted(left_over_list + list_1, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    two_pair_hand = list_2 + list_3 + left_over_list
                    return two_pair_hand, "Two Pair"
            else:
                if list_1[0][0] > list_2[0][0]:
                    left_over_list = sorted(left_over_list + list_2, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    two_pair_hand = list_3 + list_1 + left_over_list
                    return two_pair_hand, "Two Pair"
                else:
                    left_over_list = sorted(left_over_list + list_1, reverse=True)
                    left_over_list.pop()
                    left_over_list.pop()
                    two_pair_hand = list_3 + list_2 + left_over_list
                    return two_pair_hand, "Two Pair"





        # quads + pair
        # set + set
        # pair x3

    if len(set_pairs_list) == 5:
        # set + pair
        if len(list_1) == 3:
            full_house_hand = list_1 + list_2
            return full_house_hand, "Full House"
        else:
            full_house_hand = list_2 + list_1
            return full_house_hand, "Full House" \

    if len(set_pairs_list) == 4:
        # quads
        # Two pair
        if not list_2:
            #quads
            left_over_list.pop()
            left_over_list.pop()
            quad_hand = list_1 + left_over_list
            return quad_hand, "Quads"
        else:
            # two pair
            if list_1[0][0] > list_2[0][0]:
                left_over_list.pop()
                left_over_list.pop()
                two_pair_hand = list_1 + list_2 + left_over_list
                return two_pair_hand, "Two Pair"
            else:
                left_over_list.pop()
                left_over_list.pop()
                two_pair_hand = list_2 + list_1 + left_over_list
                return two_pair_hand, "Two Pair"

    if len(set_pairs_list) == 3:
        # set
        left_over_list.pop()
        left_over_list.pop()
        set_hand = list_1 + left_over_list
        return set_hand, "Three of a Kind"

    if len(set_pairs_list) == 2:
        # pair
        left_over_list.pop()
        left_over_list.pop()
        pair_hand = list_1 + left_over_list
        return pair_hand, "Pair"







test_hero = [[7, "Hearts"], [8, "Clubs"]]
test_villian = [[12, "Clubs"], [13, "Spades"]]
test_community = [[7, 'Spades'], [12, 'Spades'], [3, 'Diamonds'], [9, 'Diamonds'], [2, 'Clubs']]
test_var1_sets_etc, test_var2_left_overs = quads_sets_pairs_check(test_hero, test_community)
print(test_var1_sets_etc)
print(test_var2_left_overs)
print(sets_pair_quads_sorter(test_var1_sets_etc, test_var2_left_overs))


