def parse(s):
    return {(x, y): c == '#'
            for y, row in enumerate(s.strip().split('\n'))
            for x, c in enumerate(row.strip())
            if c != '.'}

# def dump(state):
#     for y in range(max(y for _, y in state) + 1):
#         print(''.join(['.' if (x,y) not in state else '#' if state[(x,y)] else 'L'
#                        for x in range(max(x for x, _ in state) + 1)]))

with open('inputs/11') as f:
    initial_state = parse(f.read().strip())

prev_state = None
next_state = initial_state

# def occupied_neighbours(state, seat):
#     x, y = seat
#     neighbours = [(nx, ny) for nx in range(x-1, x+2)
#                   for ny in range(y-1, y+2)
#                   if not (nx == x and ny == y)]
#     return sum(1 for pos in neighbours if pos in state and state[pos])


max_x = max(x for x, _ in initial_state.keys())
max_y = max(y for _, y in initial_state.keys())
visible_from = {}
for x, y in initial_state:
    visible_from[(x, y)] = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0: continue
            nx, ny = x + dx, y + dy
            while 0 <= nx <= max_x and 0 <= ny <= max_y:
                if (nx, ny) in initial_state:
                    visible_from[(x, y)].append((nx, ny))
                    break
                nx += dx
                ny += dy

def visibly_occupied_seats(state, seat):
     return sum(1 for other_seat in visible_from[seat] if state[other_seat])

iterations = 0
while prev_state != next_state:
    prev_state = next_state
    next_state = {}
    # print('\niteration', iterations)
    # dump(prev_state)
    for seat, occupied in prev_state.items():
        if occupied and visibly_occupied_seats(prev_state, seat) >= 5:
            next_state[seat] = False
        elif not occupied and visibly_occupied_seats(prev_state, seat) == 0:
            next_state[seat] = True
        else:
            next_state[seat] = occupied
    iterations += 1

print(sum(1 for occupied in next_state.values() if occupied))
