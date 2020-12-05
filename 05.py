#!/usr/bin/env python

def main(f):
    seat_ids = []

    for line in f:
        bp = line.strip()

        adj = 128 // 2
        low, high = 0, 127
        for c in bp[:7]:
            if c == 'B': low += adj
            else: high -= adj
            adj //= 2
        assert low == high
        row = low

        adj = 8 // 2
        low, high = 0, 7
        for c in bp[7:]:
            if c == 'R': low += adj
            else: high -= adj
            adj //= 2
        assert low == high
        col = low

        seat_id = row * 8 + col

        # print(bp[:7], bp[7:], row, col, seat_id)
        seat_ids.append(seat_id)

    # print(max(seat_ids))
    seat_ids.sort()
    for i, seat_id in enumerate(seat_ids):
        if seat_ids[i+1] != seat_id + 1:
            print(seat_id + 1)
            break

if __name__ == '__main__':
    with open('inputs/05') as f:
        main(f)
