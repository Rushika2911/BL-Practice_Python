import random

card_points = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_signs = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']

deck = []
for sign in card_signs:
    for point in card_points:
        deck.append(f"{sign}-{point}")


print("Initial Deck:")
for position, card in enumerate(deck, start=1):
    print(f"Position {position}: {card}")

initial_kings = []
for position, card in enumerate(deck):
    if "K" in card:
        initial_kings.append(position)

print("\nInitial positions of all Kings:")
print(initial_kings)

random.shuffle(deck)
print("\nShuffled Deck:")
for position, card in enumerate(deck, start=1):
    print(f"Position {position}: {card}")

shuffled_kings = []

for position, card in enumerate(deck):
    if "K" in card:
        shuffled_kings.append(position)

print("\nShuffled positions of all Kings:")
print(shuffled_kings)