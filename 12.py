with open('inputs/12') as f:
    instructions = [(l[0], int(l[1:])) for l in f]

offsets = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

def move(p, offset, scale):
    return (p[0] + offset[0] * scale, p[1] + offset[1] * scale)

bearings = ['N', 'E', 'S', 'W']

def rotate_ship(i, direction, deg):
    turns = (deg // 90) * (1 if direction == 'R' else -1)
    return (i + turns) % len(bearings)

def rotate_marker(p, direction, deg):
    # TODO: is there some matrix operation that can do this?
    turn = (lambda p: (p[1], -p[0])) if direction == 'R' else (lambda p: (-p[1], p[0]))
    for _ in range(abs(deg // 90)):
        p = turn(p)
    return p

ship_pos = (0, 0)
marker_pos = (10, 1)
bearing_idx = 1

for cmd, val in instructions:
    if cmd in offsets:
        # ship_pos = move(ship_pos, offsets[cmd], val)
        marker_pos = move(marker_pos, offsets[cmd], val)
    elif cmd == 'F':
        # ship_pos = move(ship_pos, offsets[bearings[bearing_idx]], val)
        ship_pos = move(ship_pos, marker_pos, val)
    elif cmd in ('L', 'R'):
        # bearing_idx = rotate_ship(bearing_idx, cmd, val)
        marker_pos = rotate_marker(marker_pos, cmd, val)
    else:
        raise NotImplementedError(cmd)

print(abs(ship_pos[0]) + abs(ship_pos[1]))
