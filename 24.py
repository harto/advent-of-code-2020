from functools import reduce

def parse_directions(s):
    while s:
        n = 2 if s[0] in ('n', 's') else 1
        yield s[:n]
        s = s[n:]

offsets = {
    'nw': (0, 1),
    'ne': (1, 1),
    'w': (-1, 0),
    'e': (1, 0),
    'sw': (-1, -1),
    'se': (0, -1),
}

def follow(directions):
    steps = [offsets[d] for d in directions]
    return reduce(lambda t, step: (t[0] + step[0], t[1] + step[1]), steps, (0, 0))

black_tiles = set()

with open('inputs/24') as f:
    for line in f:
        directions = parse_directions(line.strip())
        tile = follow(directions)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

print(len(black_tiles))

def neighbours(t):
    return [(t[0] + o[0], t[1] + o[1]) for o in offsets.values()]

for _ in range(100):
    next_black_tiles = set()

    for t in black_tiles:
        adjacent_black_tiles = sum(1 for n in neighbours(t) if n in black_tiles)
        if 0 < adjacent_black_tiles <= 2:
            next_black_tiles.add(t)

    white_tiles = set(n for t in black_tiles for n in neighbours(t)) - black_tiles
    for t in white_tiles:
        adjacent_black_tiles = sum(1 for n in neighbours(t) if n in black_tiles)
        if adjacent_black_tiles == 2:
            next_black_tiles.add(t)

    black_tiles = next_black_tiles

print(len(black_tiles))
