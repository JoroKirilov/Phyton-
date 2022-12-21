data_input = input().split(" ")
shuffing = int(input())
first_card = data_input[0]
last_card = data_input[-1]
cards = data_input.copy()
cards.remove(first_card)
cards.remove(last_card)
first_part = []
second_part = []
result = []
final_result = []

for n in range(shuffing):
    for idx in range((len(cards)//2)):
        first_part.append(cards[idx])
    for idx in range((len(cards)//2), len(cards)):
        second_part.append(cards[idx])

    for i in range(len(first_part)):
        result.append(second_part[i])
        result.append(first_part[i])
    cards = result.copy()
    result.clear()
    first_part.clear()
    second_part.clear()

final_result.append(first_card)
for card in cards:
    final_result.append(card)
final_result.append(last_card)

print(final_result)
