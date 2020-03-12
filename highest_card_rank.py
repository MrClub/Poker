def high_card(hole_cards, community_cards):
    high_card_hand = sorted(hole_cards + community_cards, reverse=True)
    high_card_hand.pop()
    high_card_hand.pop()
    return high_card_hand, f"High Card {high_card_hand[0][0]}"
