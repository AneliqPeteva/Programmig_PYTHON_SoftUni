deck_of_cards = input().split()
numbers_of_shuffle = int(input())
for shuffle in range(numbers_of_shuffle):
    final_desk = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    for card_index in range(len(right_part)):
        final_desk.append(left_part[card_index])
        final_desk.append(right_part[card_index])
    deck_of_cards = final_desk

print(deck_of_cards)