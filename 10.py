from collections import defaultdict

with open('inputs/10') as f:
    nums = [int(line.strip()) for line in f]

nums = [0] + sorted(nums) + [nums[-1] + 3]

dist = defaultdict(int)
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i+1]
    dist[b - a] += 1

# print(dist[1] * dist[3])

###

def arrangements(nums, cache = {}):
    if len(nums) < 2: return 1
    if nums in cache: return cache[nums]
    n = 0
    i = 1
    while i < len(nums) and nums[i] - nums[0] <= 3:
        n += arrangements(nums[i:], cache)
        i += 1
    cache[nums] = n
    return n

print(arrangements(tuple(nums)))
