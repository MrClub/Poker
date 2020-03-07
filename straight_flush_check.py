# - this checks for a flush, then checks all flush cards if there is 5 or more and returns the best straight flush.
# - if no flsuh or straight flush checks for a straight.

"""import flush_check as flush
import straight_check as straight"""



test_hero = [[2,"Hearts"],[3,"Clubs"]]
test_villian = [[8,"Hearts"],[10,"Hearts"]]
test_community = [[4, 'Hearts'], [7, 'Spades'], [6, 'Hearts'], [11, 'Clubs'], [12, 'Hearts']]


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
            return straight_check(diamonds)
        else:
            diamonds = sorted(diamonds,reverse=True)
            if len(diamonds) == 6 or len(diamonds) == 7:
                diamonds = flush_ranking(diamonds)
            return diamonds
    if len(hearts) >= 5:
        if straight_check(hearts):
            return straight_check(hearts)
        else:
            hearts = sorted(hearts,reverse=True)
            if len(hearts) == 6 or len(hearts) == 7:
                hearts = flush_ranking(hearts)
            return hearts
    if len(spades) >= 5:
        if straight_check(spades):
            return straight_check(spades)
        else:
            spades = sorted(spades,reverse=True)
            if len(spades) == 6 or len(spades) == 7:
                spades = flush_ranking(spades)
            return spades
    if len(clubs) >= 5:
        if straight_check(clubs):
            return straight_check(clubs)
        else:
            clubs = sorted(clubs,reverse=True)
            if len(clubs) == 6 or len(clubs) == 7:
                clubs = flush_ranking(clubs)
            return clubs
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

straight_flush_check(test_hero,test_community)
