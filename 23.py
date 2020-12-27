### part 1

cups = [int(x) for x in '219347865']

for _ in range(100):
    c, *rest = cups[:4]
    cups = cups[4:]
    dest_val = c - 1
    while dest_val in rest and dest_val > 0:
        dest_val -= 1
    if dest_val <= 0:
        dest_val = max(cups)
    i = cups.index(dest_val)
    cups = cups[:i+1] + rest + cups[i+1:] + [c]

i = cups.index(1)
print(''.join([str(cups[(i + 1 + j) % len(cups)]) for j in range(len(cups) - 1)]))

### part 2

cups = [int(x) for x in '219347865'] + list(range(10, 1000001))
nexts = { cups[i]: (cups[i+1] if i < len(cups) - 1 else cups[0]) for i in range(len(cups)) }

c = cups[0]
for _ in range(10000000):
    x = nexts[c]
    y = nexts[x]
    z = nexts[y]

    next_c = nexts[z]

    insert_after = c - 1
    while insert_after in (x, y, z) and insert_after > 0:
        insert_after -= 1
    if insert_after <= 0:
        insert_after = max(n for n in range(999997, 1000001) if n not in (x, y, z))
    insert_before = nexts[insert_after]

    nexts[insert_after] = x
    nexts[z] = insert_before

    nexts[c] = next_c
    c = next_c

x = nexts[1]
y = nexts[x]
print(x, y, x * y)
