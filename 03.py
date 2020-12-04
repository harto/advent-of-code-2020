#!/usr/bin/env python

from functools import reduce

def tree_count(m, slope_x, slope_y):
    trees = 0
    x = slope_x
    for y in range(slope_y, len(m), slope_y):
        if m[y][x] == '#':
            trees += 1
        x = (x + slope_x) % len(m[y])
    return trees

def main(m):
    trees = reduce(
        lambda acc, x: acc * x,
        (tree_count(m, slope_x, slope_y) for slope_x, slope_y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))
    )
    print(trees)

if __name__ == '__main__':
    with open('inputs/03') as f:
        main([l.strip() for l in f])
