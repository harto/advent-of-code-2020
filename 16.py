with open('inputs/16') as f:
    sections = f.read().strip().split('\n\n')

import re
rules = { name: ((int(a), int(b)), (int(c), int(d)))
          for name, a, b, c, d in [re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
                                   for line in sections[0].split('\n')] }

my_ticket = [int(x) for x in sections[1].split('\n')[1].split(',')]
nearby_tickets = [[int(x) for x in line.split(',')]
                  for line in sections[2].split('\n')[1:]]

def satisfies(rule, value):
    return any(lower <= value <= upper for lower, upper in rule)

error_rate = 0
for ticket in nearby_tickets:
    for value in ticket:
        if not any(satisfies(rule, value) for rule in rules.values()):
            error_rate += value
print(error_rate)

###

valid_tickets = [ticket for ticket in nearby_tickets
                 if all(any(satisfies(rule, value) for rule in rules.values())
                        for value in ticket)]

possible_positions = { rule_name: set(range(len(my_ticket))) for rule_name in rules }

for ticket in valid_tickets:
    for i, value in enumerate(ticket):
        for rule_name, rule in rules.items():
            if i in possible_positions[rule_name] and not satisfies(rule, value):
                possible_positions[rule_name].remove(i)

known_positions = {}
while possible_positions:
    rule_name, positions = min(possible_positions.items(), key=lambda item: len(item[1]))
    assert(len(positions) == 1)
    position = next(iter(positions))
    known_positions[rule_name] = position
    del possible_positions[rule_name]
    for other_rule_name, other_positions in possible_positions.items():
        if position in other_positions:
            other_positions.remove(position)

from functools import reduce
print(reduce(int.__mul__, (my_ticket[i]
                           for field_name, i in known_positions.items()
                           if field_name.startswith('departure'))))
