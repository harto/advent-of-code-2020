with open('inputs/20') as f:
    sections = f.read().strip().split('\n\n')

import re
tiles = {}
for section in sections:
    lines = section.split('\n')
    tid = int(re.match(f'Tile (\d+)', lines[0]).group(1))
    tiles[tid] = lines[1:]

def edges(t):
    return [t[0], t[-1], ''.join(row[0] for row in t), ''.join(row[-1] for row in t)]

def match(a, b):
    return set(edges(a)) & (set(edges(b)) | set(e[::-1] for e in edges(b)))

from collections import defaultdict
neighbours = defaultdict(set)
for tid, tile in tiles.items():
    for other_tid, other_tile in tiles.items():
        if tid != other_tid and match(tile, other_tile):
            neighbours[tid].add(other_tid)
            neighbours[other_tid].add(tid)

from functools import reduce
print(reduce(int.__mul__, (id for id, neighbour_ids in neighbours.items()
                           if len(neighbour_ids) == 2)))
