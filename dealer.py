# This is a place to add all my functions

import random

deck_of_cards = []


def deck_builder(suit, list):
    # builds the deck because I'm too lazy to type everything out
    suit_list = []
    for n in range(2, 15):
        list.append([n, suit])
    return list


deck_builder("Diamonds", deck_of_cards)
deck_builder("Hearts", deck_of_cards)
deck_builder("Clubs", deck_of_cards)
deck_builder("Spades", deck_of_cards)

# test




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
    # show villians hand if show_villian is set to "y"
    show_player_hand(player_hand, "hero")
    if show_villian == "y":
        show_player_hand(villian_hand,"villian")
    else:
        pass
    show_the_board(board)