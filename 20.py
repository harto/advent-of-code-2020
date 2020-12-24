from collections import defaultdict
from itertools import chain
from functools import reduce

with open('inputs/20') as f:
    sections = f.read().strip().split('\n\n')

import re
tiles = {}
for section in sections:
    lines = section.split('\n')
    tid = int(re.match(f'Tile (\d+)', lines[0]).group(1))
    tiles[tid] = lines[1:]

def rotate(tile):
    rotated = [[None] * len(row) for row in tile]
    for y, row in enumerate(tile):
        for x, v in enumerate(row):
            rotated[x][len(tile)-1-y] = v
    return [''.join(row) for row in rotated]

def flip(tile):
    return list(reversed(tile))

def edges(t):
    return [t[0],
            ''.join(row[-1] for row in t),
            ''.join(t[-1])[::-1],
            ''.join(row[0] for row in t)[::-1]]

def match(a, b):
    a_edges = edges(a)
    b_edges = edges(b)
    for i, a_edge in enumerate(a_edges):
        try:
            j = b_edges.index(a_edge[::-1])
        except ValueError:
            continue
        else:
            rotations = (2 - (j - i)) % 4
            assert rotations in range(4), rotations
            for x in range(rotations):
                b = rotate(b)
            return i, b

neighbours = defaultdict(dict) # id -> { 0: up_id, 1: right_id, 2: down_id, 3: left_id }
reoriented = {}

# Start with one tile and expand outward - this way we don't end up trying to
# connect disparate sets of differently-oriented tiles.
remaining = [next(iter(tiles))]
while remaining:
    tid = remaining.pop()
    matched = False
    for other_tid in tiles:
        if tid == other_tid or tid in neighbours[other_tid].values():
            continue
        tile = reoriented.get(tid) or tiles[tid]
        other_tile = reoriented.get(other_tid) or tiles[other_tid]
        m = match(tile, other_tile) or match(tile, flip(other_tile))
        if m:
            side, rotated_tile = m
            other_side = (side + 2) % 4
            assert side not in neighbours[tid], \
                f'{tid} already matched to {neighbours[tid][side]} on side {side}'
            neighbours[tid][side] = other_tid
            assert other_side not in neighbours[other_tid], \
                f'{other_tid} already matched to {neighbours[other_tid][other_side]} on side {other_side}'
            neighbours[other_tid][other_side] = tid
            reoriented[tid] = tile
            assert other_tid not in reoriented or reoriented[other_tid] == rotated_tile
            reoriented[other_tid] = rotated_tile
            remaining.append(other_tid)

# part 1
# print(reduce(int.__mul__, (id for id, neighbour_ids in neighbours.items()
#                            if len(neighbour_ids) == 2)))

import math
rows = cols = int(math.sqrt(len(neighbours)))

layout = [[None] * cols for _ in range(rows)]
top_left_tid = next(tid for tid, neighbour_tids in neighbours.items()
                    if set(neighbour_tids) == {1, 2})
remaining = [(top_left_tid, 0, 0)]
while remaining:
    tid, x, y = remaining.pop(0)
    if layout[y][x]: continue
    layout[y][x] = tid
    neighbour_tids = neighbours[tid]
    if 1 in neighbours[tid]: # right
        remaining.append((neighbours[tid][1], x+1, y))
    if 2 in neighbours[tid]: # down
        remaining.append((neighbours[tid][2], x, y+1))

# print('\n'.join(' '.join(str(tid) for tid in row) for row in layout))

a_tile = list(tiles.values())[0]
th = len(a_tile) - 2 # trim borders
tw = len(a_tile[0]) - 2 # trim borders

image = [[None] * cols * tw for _ in range(rows * th)]
for y, row in enumerate(layout):
    for x, tid in enumerate(row):
        for ty, trow in enumerate(reoriented[tid][1:-1]):
            for tx, pixel in enumerate(trow[1:-1]):
                image[y * th + ty][x * tw + tx] = pixel

monster = [row for row in '''
                  #
#    ##    ##    ###
 #  #  #  #  #  #
'''.split('\n') if row != '']

monster_offsets = [(x, y)
                   for y, row in enumerate(monster)
                   for x, c in enumerate(row)
                   if c == '#']

def count_monsters(image):
    locations = [(x, y) for y, row in enumerate(image)
                 for x in range(len(row))
                 if monster_at(image, x, y)]
    print(locations)
    return len(locations)

def monster_at(image, x, y):
    for dx, dy in monster_offsets:
        ix = x + dx
        iy = y + dy
        if not (0 <= iy < len(image) and 0 <= ix < len(image[iy]) and image[iy][ix] == '#'):
            return False
    return True

for i in range(8):
    monsters_found = count_monsters(image)
    if monsters_found:
        break
    image = rotate(image)
    if i == 3:
        image = flip(image)

assert monsters_found

all_squares = len([c for row in image for c in row if c == '#'])
print(all_squares - monsters_found * len(monster_offsets))

###

import unittest
class Tests(unittest.TestCase):
    def test_flip(self):
        self.assertEqual(['xx',
                          'ab'],
                         flip(['ab',
                               'xx']))

    def test_rotate(self):
        t = ['ab',
             'xx']
        self.assertEqual(['xa',
                          'xb'], rotate(t))
        self.assertEqual(['xx',
                          'ba'], rotate(rotate(t)))
        self.assertEqual(['bx',
                          'ax'], rotate(rotate(rotate(t))))
        self.assertEqual(t, rotate(rotate(rotate(rotate(t)))))

    def test_edges(self):
        t = ['abc',
             'def',
             'ghi']
        self.assertEqual(['abc', 'cfi', 'ihg', 'gda'], edges(t))

    def test_match(self):
        t1 = ['xx',
              'ab']
        t2 = ['ab',
              'yy']

        self.assertEqual((2, t2), match(t1, t2))
        self.assertEqual((2, t2), match(t1, rotate(t2)))
        self.assertEqual((2, t2), match(t1, rotate(rotate(t2))))
        self.assertEqual((2, t2), match(t1, rotate(rotate(rotate(t2)))))
