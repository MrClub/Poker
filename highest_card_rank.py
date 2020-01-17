# This will rank a hand based on who has the highest card. If both are the same
# it will check the kicker. and if they are both the same it will call a tie.

import random
import dealer


deck_of_cards = []

dealer.deck_builder("Diamonds", deck_of_cards)
dealer.deck_builder("Hearts", deck_of_cards)
dealer.deck_builder("Clubs", deck_of_cards)
dealer.deck_builder("Spades", deck_of_cards)

print(deck_of_cards)
print(len(deck_of_cards))
random.shuffle(deck_of_cards)
burned = []
hero_hand = []
villian_hand = []

dealer.deal(1,deck_of_cards,burned)
dealer.deal(2,deck_of_cards,hero_hand)
dealer.deal(2,deck_of_cards,villian_hand)

print("Hero's:",hero_hand , "\n" , "Villian's:", villian_hand)

def highest_card(heros_hand,villians_hand):
    heros_highest = 0
    heros_lowest = 0
    villians_highest = 0
    villians_lowest = 0
    for card in hero_hand:
        if card[0] > heros_highest:
            heros_lowest = heros_highest
            heros_highest = card[0]
        else:
            heros_lowest = card[0]
    for card in villians_hand:
        if card[0] > villians_highest:
            villians_lowest = villians_highest
            villians_highest = card[0]
        else:
            villians_lowest = card[0]

    if heros_highest > villians_highest:
        print("Hero wins with:", hero_hand)
    elif villians_highest > heros_highest:
        print("Villian wins with:", villian_hand)
    else:
        if heros_lowest > villians_lowest:
            print("Hero wins with:", hero_hand)
        else:
            if villians_lowest > heros_lowest:
                print("Villian wins with:", villian_hand)
            else:
                print("Split Pot")

highest_card(hero_hand,villian_hand)


print(len(deck_of_cards))