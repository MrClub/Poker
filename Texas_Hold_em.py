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



def deal(howmany, deck, list):
    # deals how many cards you want to a selected list
    for n in range(0, howmany):
        list.append(deck.pop())
    return list


def show_player_hand(hand_list, player):
    # show the player's hand
    if player == "hero":
        print("Your hand".center(22, "-"))
    else:
        print("Villian's hand".center(22, "-"))
    for card in hand_list:
        print(str(card[0]) + " of " + card[1])
    print()


def show_the_board(board_list):
    # shows the board i.e. community cards
    print("The board".center(22, "-"))
    for card in board_list:
        print(str(card[0]) + " of " + card[1])
    print()


def state_of_game(player_hand, villian_hand, board,show_villian):
    # combines show_the_board and show_player_hand_function into one
    # show villians hand is show_villian is set to "y"
    show_player_hand(player_hand, "hero")
    if show_villian == "y":
        show_player_hand(villian_hand,"villian")
    else:
        pass
    show_the_board(board)




while True:
    print(len(deck_of_cards))
    print("Play or quit?")
    play = input()
    if play == "quit":
        break
    hero = []
    villian_1 = []
    board = []
    discarded = []
    random.shuffle(deck_of_cards)
    print("Let's play!")
    deal(1, deck_of_cards, discarded)
    deal(2, deck_of_cards, hero)
    deal(2, deck_of_cards, villian_1)
    show_player_hand(hero,"hero")
    play = input("Play or fold?")
    if play == "fold":
        deck_of_cards += discarded + board + hero + villian_1
        continue
    deal(1, deck_of_cards, discarded)
    deal(3, deck_of_cards, board)
    state_of_game(hero,villian_1, board, "n")
    play = input("Play or fold?")
    if play == "fold":
        deck_of_cards += discarded + board + hero + villian_1
        continue
    deal(1, deck_of_cards, discarded)
    deal(1, deck_of_cards, board)
    state_of_game(hero,villian_1, board,"n")
    play = input("Play or fold?")
    if play == "fold":
        deck_of_cards += discarded + board + hero + villian_1
        continue
    deal(1, deck_of_cards, discarded)
    deal(1, deck_of_cards, board)
    state_of_game(hero,villian_1, board, "y")

    deck_of_cards += discarded + board + hero + villian_1
