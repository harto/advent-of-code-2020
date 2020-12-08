from functools import reduce

with open('inputs/06') as f:
    groups = f.read().strip().split('\n\n')

# group_responses = [
#     reduce(set.union, (set(responses) for responses in group.split('\n')))
#     for group groups
# ]

group_responses = [
    reduce(set.intersection, (set(responses) for responses in group.split('\n')))
    for group in groups
]

print(sum(len(x) for x in group_responses))
