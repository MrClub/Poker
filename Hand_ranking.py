def hand_ranking(player_hand,board):
    # this will rank the hand. https://en.wikipedia.org/wiki/List_of_poker_hands
    # Straight Flush
    # Four of a Kind
    # Full House
    # Flush
    # Straight
    # Three of a Kind
    # Two Pair
    # One Pair
    # High Card

    hand_ranks = {}
    hand_values =[]
    board +=player_hand
    board = sorted(board)
    print(board)
    for e in board:
        hand_values.append(e[0])
        #this organises a dictionary and counts the values of the hands
        for n in e:
            if n not in hand_ranks:
                hand_ranks[n]=0
            hand_ranks[n] +=1
    print(hand_ranks)
    print(hand_values)
    is_this_a_straight, the_straight = straight_check(hand_values)
    pairs = 0
    threes = 0
    for entry in hand_ranks:
        # this figures out the highest hand ranking by iterating through the dictionary
        if is_this_a_straight is True and hand_ranks[entry] == 5:
            return print("STRAIGHT FLUSH")
        if hand_ranks[entry] == 4:
            return print("Four of a Kind of " + str(entry) +"'s")
        if hand_ranks[entry] == 5:
            return print("Flush of " + entry)
        if is_this_a_straight:
            return print("A straight of" ,the_straight )
        if hand_ranks[entry] == 3:
            threes += 1
        if hand_ranks[entry] == 2:
            pairs += 1

        if threes ==1 and pairs >=1:
            return print("Full House")
        if threes == 1:
            return print("Three of a kind")
        if pairs == 2:
            return print("Two pair")
        if pairs == 1:
            return print("One Pair")

def straight_check(board_list):
    # This checks for a straight in a 7 card list and returns the highest possible straight and True.
    possible_straights = [
                          [10, 11, 12, 13, 1], [9, 10, 11, 12, 13], [8, 9, 10, 11, 12], [7, 8, 9, 10, 11],
                          [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7], [2, 3, 4, 5, 6],
                          [1, 2, 3, 4, 5]
                         ]

    for straight in possible_straights:
        count = 0
        for number in straight:
            if number in board_list:
                count += 1
            if count == 5:
                return True, straight
    return False, []


test_deck = [[2, 'Diamonds'],[3, 'Hearts']]
test_board = [[1, 'Hearts'], [13, 'Hearts'], [12, 'Hearts'], [11, 'Hearts'],[10, 'Hearts']]
hand_ranking(test_deck,test_board)