with open('inputs/17') as f:
    state = {(x, y, 0, 0): c == '#' for y, line in enumerate(f) for x, c in enumerate(line)}

def find_neighbours(cell):
    x, y, z, w = cell
    return [(nx, ny, nz, nw)
            for nx in range(x - 1, x + 2)
            for ny in range(y - 1, y + 2)
            for nz in range(z - 1, z + 2)
            for nw in range(w - 1, w + 2)
            if not (nx == x and ny == y and nz == z and nw == w)]

for i in range(6):
    next_state = {}
    cells = { n for cell in state for n in find_neighbours(cell) }
    for cell in cells:
        active_neighbours = len([n for n in find_neighbours(cell) if state.get(n)])
        next_state[cell] = active_neighbours in (2, 3) if state.get(cell) \
            else active_neighbours == 3
    state = next_state

print(len([cell for cell in state if state[cell]]))
