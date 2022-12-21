cards = input().split()
n_shuffle = int(input())
half = (len(cards) // 2)
shuffled_card = []
first_card = cards[0]
last_Card = cards[-1]
cards.pop()
cards.pop(0)
for _ in range(n_shuffle):
    left_cards = cards[:half - 1]
    right_cards = cards[half - 1:len(cards)]
    for idx in range(len(left_cards)):
        shuffled_card.append(right_cards[idx])
        shuffled_card.append(left_cards[idx])

    cards = shuffled_card.copy()
    shuffled_card = []

shuffled_card.append(first_card)
for idx in range(len(cards)):
    shuffled_card.append(cards[idx])
shuffled_card.append(last_Card)

print(shuffled_card)




