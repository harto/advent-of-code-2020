inputs = [2, 0, 1, 7, 4, 14, 18]

from collections import defaultdict
spoken_indices = defaultdict(list)

for i, n in enumerate(inputs):
    spoken_indices[n].append(i)

last_spoken = n

for i in range(len(inputs), 30000000):
    if len(spoken_indices[last_spoken]) < 2:
        spoken = 0
    else:
        spoken = spoken_indices[last_spoken][-1] - spoken_indices[last_spoken][-2]
    spoken_indices[spoken].append(i)
    last_spoken = spoken

print(last_spoken)
