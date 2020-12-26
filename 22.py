with open('inputs/22') as f:
    s = f.read()

decks = []
for deck in s.strip().split('\n\n'):
    decks.append([int(card) for card in deck.split('\n')[1:]])

# while all(decks):
#     c0 = decks[0].pop(0)
#     c1 = decks[1].pop(0)
#     if c0 > c1:
#         decks[0].append(c0)
#         decks[0].append(c1)
#     else:
#         decks[1].append(c1)
#         decks[1].append(c0)
#
# winning_deck = next(d for d in decks if d)

def play(decks):
    d0, d1 = decks
    seen = set()
    while all(decks):
        if (tuple(d0), tuple(d1)) in seen:
            return 0, decks
        seen.add((tuple(d0), tuple(d1)))
        c0 = d0.pop(0)
        c1 = d1.pop(0)
        if c0 <= len(d0) and c1 <= len(d1):
            winner, _ = play([d0[:c0], d1[:c1]])
        else:
            winner = 0 if c0 > c1 else 1
        if winner == 0:
            d0.extend((c0, c1))
        else:
            d1.extend((c1, c0))
    return (0 if d0 else 1), decks

winner, decks = play(decks)
winning_deck = decks[winner]

print(sum(n * (i + 1) for i, n in enumerate(reversed(winning_deck))))
