# This will rank each hand. It will pull all the individual checks ie flush_check, straight_check, highest_card_rank into a
# coherent whole

# TODO tidy up the return functions in flush_check and straight check to include a 2nd variable with hand name


test_hero = [[13,"Hearts"],[12,"Hearts"]]
test_villian = [[8,"Hearts"],[10,"Hearts"]]
test_community = [[3, 'Clubs'], [8, 'Spades'], [14, 'Hearts'], [11, 'Hearts'], [10, 'Hearts']]

def hand_rank(hole_cards, community_cards):
    # Will pull all individual hand rank checks together.

    if sfc.straight_flush_check(hole_cards,community_cards):
        print(sfc.straight_flush_check(hole_cards,community_cards))

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
    if not sets_pairs_list:
        return [], left_overs
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

def straight_flush_check(hole_cards,community_cards):
    merged_cards = sorted(hole_cards+community_cards)
    if flush_check(merged_cards):
        print(flush_check(merged_cards))
    else:
        print(straight_check(merged_cards))


def flush_check(merged_cards):
    # checks for flush, if more than five cards returns best.
    diamonds = []
    hearts = []
    spades = []
    clubs = []
    #merged_cards = sorted(hole_cards+community_cards)
    for card in merged_cards:
        if card[1] == "Diamonds":
            diamonds.append(card)
        elif card[1] == "Hearts":
            hearts.append(card)
        elif card[1] == "Spades":
            spades.append(card)
        else:
            clubs.append(card)

    if len(diamonds) >= 5:
        if straight_check(diamonds):
            # this checks for a straight in the suited cards
            return straight_check(diamonds), "Straight Flush"
        else:
            diamonds = sorted(diamonds,reverse=True)
            if len(diamonds) == 6 or len(diamonds) == 7:
                diamonds = flush_ranking(diamonds)
            return diamonds, "Flush"
    if len(hearts) >= 5:
        if straight_check(hearts):
            return straight_check(hearts), "Straight Flush"
        else:
            hearts = sorted(hearts,reverse=True)
            if len(hearts) == 6 or len(hearts) == 7:
                hearts = flush_ranking(hearts)
            return hearts, "Flush"
    if len(spades) >= 5:
        if straight_check(spades):
            return straight_check(spades), "Straight Flush"
        else:
            spades = sorted(spades,reverse=True)
            if len(spades) == 6 or len(spades) == 7:
                spades = flush_ranking(spades)
            return spades, "Flush"
    if len(clubs) >= 5:
        if straight_check(clubs):
            return straight_check(clubs), "Straight Flush"
        else:
            clubs = sorted(clubs,reverse=True)
            if len(clubs) == 6 or len(clubs) == 7:
                clubs = flush_ranking(clubs)
            return clubs, "Flush"
    return []



def flush_ranking(flush_list):
    # take a flush of 5 greater cards and trims it to best five
    if len(flush_list) ==6:
        flush_list.pop()
    if len(flush_list) == 7:
        flush_list.pop()
        flush_list.pop()
    return flush_list

def compare_flushes(flush_one, flush_two):
    # compare to flushes and returns the best, if tie returns empty list
    flush_one = sorted(flush_one,reverse=True)
    flush_two = sorted(flush_two,reverse=True)
    if flush_one[0][0] == flush_two[0][0]:
        return []
    elif flush_one[0][0] > flush_two[0][0]:
        return flush_one
    else:
        return flush_two

def compare_straights(straight_one, straight_two):
    # compares two straights and returns the best
    if straight_one[0][0] > straight_two[0][0]:
        return straight_one
    elif straight_two[0][0] > straight_one[0][0]:
        return straight_two
    else:
        return []


def straight_check(merged_cards):
    #finds best straight and returns it, else returns empty list
    count = 0
    straight_number = merged_cards[0][0]
    straight_list =[]
    #print(merged_cards)
    for card in merged_cards:
        if wheel_straight_check(merged_cards,straight_list):
            straight_list.append(merged_cards[-1])
            break
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

    # below check the straight length and trims it to the best five
    if len(straight_list) < 5:
        straight_list =[]
        return []
    if len(straight_list) == 6:
        straight_list = sorted(straight_list, reverse=True)
        straight_list.pop()
    if len(straight_list) == 7:
        straight_list = sorted(straight_list, reverse=True)
        straight_list.pop()
        straight_list.pop()
    straight_list=sorted(straight_list,reverse=True)

    return straight_list

def wheel_straight_check(merged_cards,straight_list):
    if len(straight_list) == 4:  # this is to check if 2,3,4,5 and there is an ace and no 6. ie wheel straight
        if straight_list[0][0] == 2:
            for card in merged_cards:
                if card[0] == 6:
                    return False
            if merged_cards[-1][0] ==14:
                return True
    else:
        return False

def high_card(hole_cards, community_cards):
    high_card_hand = sorted(hole_cards + community_cards, reverse=True)
    high_card_hand.pop()
    high_card_hand.pop()
    return high_card_hand, f"High Card {high_card_hand[0][0]}"

hand_rank(test_hero,test_community)

