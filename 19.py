with open('inputs/19') as f:
    inp = f.read()

rule_text, message_text = inp.split('\n\n')

rules = {}
for line in rule_text.split('\n'):
    k, rest = line.split(': ')
    if rest.startswith('"'):
        v = rest[1:2]
    else:
        v = tuple(tuple(int(n) for n in option.split(' ')) for option in rest.split(' | '))
    rules[int(k)] = v

def matches(rules, i, msg):
    rule = rules[i]
    if isinstance(rule, str):
        if msg and msg[0] == rule:
            return (msg[1:],)
        else:
            return ()
    match_remainders = ()
    for option in rule:
        partial_matches = (msg,)
        for j in option:
            partial_matches = tuple(match for remaining in partial_matches
                                    for match in matches(rules, j, remaining))
        match_remainders += partial_matches
    return match_remainders

# part 2
rules[8] = ((42,), (42, 8))
rules[11] = ((42, 31), (42, 11, 31))

print(len([match for match in (matches(rules, 0, msg) for msg in message_text.split('\n'))
           if '' in match]))
