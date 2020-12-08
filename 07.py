from collections import defaultdict
import re

# containers_of = defaultdict(set)
contents_of = defaultdict(list)

with open('inputs/07') as f:
    for line in f:
        container, rest = line.strip().split(' contain ', 2)
        container = container.removesuffix('s')
        for s in rest.removesuffix('.').split(', '):
            m = re.match('(\d+) (.+?)s?$', s)
            if not m: continue
            n, bag_type = m.groups()
            # containers_of[bag_type].add(container)
            contents_of[container].append((bag_type, int(n)))

# all_containers = set()
# remaining = ['shiny gold bag']
# while remaining:
#     bag_type = remaining.pop()
#     containers = containers_of[bag_type]
#     all_containers |= containers
#     remaining.extend(containers)
# print(len(all_containers))

count = 0
remaining = contents_of['shiny gold bag']
while remaining:
    bag_type, n = remaining.pop()
    count += n
    remaining.extend(contents_of[bag_type] * n)
print(count)
