with open('inputs/14') as f:
    prog = [l.strip().split(' = ', 2) for l in f.readlines()]

###

mask0 = mask1 = 0
mem = {}

for lhs, rhs in prog:
    if lhs == 'mask':
        mask0 = int(''.join('0' if c == '0' else '1' for c in rhs), 2)
        mask1 = int(''.join('1' if c == '1' else '0' for c in rhs), 2)
    else:
        addr = int(lhs[4:-1])
        val = int(rhs)
        mem[addr] = val & mask0 | mask1

print(sum(mem.values()))

###

def mask_addresses(addr, mask):
    masked = [addr]
    for i, c in enumerate(mask):
        if c == '0': continue
        bit = 1 << (35 - i)
        if c == '1': masked = [a | bit for a in masked]
        if c == 'X': masked = [a | bit for a in masked] + [a & ~bit for a in masked]
    return masked

mask = None
mem = {}

for lhs, rhs in prog:
    if lhs == 'mask':
        mask = rhs
    else:
        addr = int(lhs[4:-1])
        val = int(rhs)
        for masked_addr in mask_addresses(addr, mask):
            mem[masked_addr] = val

print(sum(mem.values()))
