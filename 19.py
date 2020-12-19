with open('inputs/19') as f:
    inp = f.read()

rule_text, message_text = inp.split('\n\n')

rules = {}
for line in rule_text.split('\n'):
    k, rest = line.split(': ')
    if rest.startswith('"'):
        v = rest[1:2]
    else:
        v = tuple(tuple(int(n) for n in alt.split(' ')) for alt in rest.split(' | '))
    rules[int(k)] = v

def matches(rules, i, msg):
    rule = rules[i]
    if isinstance(rule, str):
        return (True, msg[1:]) if (msg and msg[0] == rule) else False
    for alt in rules[i]:
        remaining = msg
        match = True
        for j in alt:
            res = matches(rules, j, remaining)
            if res:
                remaining = res[1]
            else:
                match = False
                break
        if match:
            return True, remaining
    return False

print(len([match for match in (matches(rules, 0, msg) for msg in message_text.split('\n'))
           if match and not match[1]]))
