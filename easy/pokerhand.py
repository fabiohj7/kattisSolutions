hand = input().split()
count = {}

for card in hand:
    if card[0] in count:
        count[card[0]] += 1
    else:
        count[card[0]] = 1

print(max(count.values()))
