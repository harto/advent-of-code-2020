def parse(s):
    return {(x, y): c == '#'
            for y, row in enumerate(s.strip().split('\n'))
            for x, c in enumerate(row)
            if c != '.'}

with open('inputs/11') as f:
    initial_seats = parse(f.read().strip())

width = max(x for x, _ in initial_seats) + 1
height = max(y for _, y in initial_seats) + 1

def dump(seats):
    return '\n'.join(''.join(['.' if (x, y) not in seats else '#' if seats[(x, y)] else 'L'
                              for x in range(width)])
                     for y in range(height))

neighbour_offsets = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)
                     if not (x == 0 and y == 0)]

# def occupied_neighbours(seats, pos):
#     x, y = pos
#     neighbours = [(x + dx, y + dy) for dx, dy in neighbour_offsets]
#     return sum(1 for pos in neighbours if pos in seats and seats[pos])

visible_from = {}
for sx, sy in initial_seats:
    visible_from[(sx, sy)] = []
    for dx, dy in neighbour_offsets:
        x = sx + dx
        y = sy + dy
        while 0 <= x < width and 0 <= y < height:
            if (x, y) in initial_seats:
                visible_from[(sx, sy)].append((x, y))
                break
            x += dx
            y += dy

def visibly_occupied(seats, pos):
     return sum(1 for seen_pos in visible_from[pos] if seats[seen_pos])

def should_occupy(seats, pos):
    currently_occupied = seats[pos]
    # occupied_others = occupied_neighbours(seats, pos)
    # if currently_occupied and occupied_others >= 4:
    occupied_others = visibly_occupied(seats, pos)
    if currently_occupied and occupied_others >= 5:
        return False
    elif not currently_occupied and occupied_others == 0:
        return True
    else:
        return currently_occupied

prev_seats = None
curr_seats = initial_seats

while prev_seats != curr_seats:
    prev_seats = curr_seats
    curr_seats = { pos: should_occupy(prev_seats, pos) for pos in prev_seats }

print(sum(1 for occupied in curr_seats.values() if occupied))
