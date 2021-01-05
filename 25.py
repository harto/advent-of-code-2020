# pubkeys = (5764801, 17807724)
pubkeys = (3418282, 8719412)

def derive_loop(pubkey):
    value = 7
    loop = 1
    while value != pubkey:
        value = (value * 7) % 20201227
        loop += 1
    return loop

loops = [derive_loop(pubkey) for pubkey in pubkeys]

print([pow(pubkey, loop, mod=20201227) for pubkey, loop in zip(pubkeys, reversed(loops))])
