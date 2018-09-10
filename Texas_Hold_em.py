import random

deck_of_cards = []


def deck_builder(suit, list):
    # builds the deck because I'm too lazy to type everything out
    suit_list = []
    for n in range(1, 14):
        list.append([n, suit])
    return list


deck_builder("Diamonds", deck_of_cards)
deck_builder("Hearts", deck_of_cards)
deck_builder("Clubs", deck_of_cards)
deck_builder("Spades", deck_of_cards)

# test

print(deck_of_cards)

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
    board +=player_hand
    board = sorted(board)
    print(board)
    for e in board:
        #this organises a dictionary and counts the values of the hands
        for n in e:
            if n not in hand_ranks:
                hand_ranks[n]=0
            hand_ranks[n] +=1
    print(hand_ranks)
    pairs = 0
    threes = 0
    for entry in hand_ranks:
        # this figures out the highest hand ranking by iterating through the dictionary
        if hand_ranks[entry] == 4:
            return print("Four of a Kind of " + str(entry) +"'s")
        if hand_ranks[entry] == 5:
            return print("Flush of " + entry)
        if hand_ranks[entry] == 3:
            threes += 1
        if hand_ranks[entry] == 2:
            pairs += 1

        if threes ==1 and pairs >=1:
            return print("Full House")



test_deck = [[2, 'Diamonds'],[2, 'Hearts']]
test_board = [[8, 'Hearts'], [5, 'Hearts'], [4, 'Hearts'], [2, 'Spades'],[2, 'Clubs']]
hand_ranking(test_deck,test_board)

def deal(howmany, deck, list):
    # deals how many cards you want to a selected list
    for n in range(0, howmany):
        list.append(deck.pop())
    return list


def show_player_hand(hand_list):
    # show the player's hand
    print("Your hand".center(22, "-"))
    for card in hand_list:
        print(str(card[0]) + " of " + card[1])
    print()


def show_the_board(board_list):
    # shows the board i.e. community cards
    print("The board".center(22, "-"))
    for card in board_list:
        print(str(card[0]) + " of " + card[1])
    print()


def state_of_game(player_hand, board):
    # combines show_the_board and show_player_hand_function into one
    show_player_hand(player_hand)
    show_the_board(board)




while True:
    print(len(deck_of_cards))
    print("Play or quit?")
    play = input()
    if play == "quit":
        break
    player_hand = []
    board = []
    discarded = []
    random.shuffle(deck_of_cards)
    print("Let's play!")
    deal(1, deck_of_cards, discarded)
    deal(2, deck_of_cards, player_hand)
    show_player_hand(player_hand)
    play = input("Play or fold?")
    if play == "fold":
        deck_of_cards += discarded + board + player_hand
        continue
    deal(1, deck_of_cards, discarded)
    deal(3, deck_of_cards, board)
    state_of_game(player_hand, board)
    play = input("Play or fold?")
    deal(1, deck_of_cards, discarded)
    deal(1, deck_of_cards, board)
    state_of_game(player_hand, board)
    play = input("Play or fold?")
    deal(1, deck_of_cards, discarded)
    deal(1, deck_of_cards, board)
    state_of_game(player_hand, board)

    deck_of_cards += discarded + board + player_hand
