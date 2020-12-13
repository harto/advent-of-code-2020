earliest_departure = 1008713
inp = '13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'

###

routes = [int(s) for s in inp.split(',') if s != 'x']

best_route = None
best_departure = None

from math import ceil
def first_departure_after(t, headway):
    return ceil(t / headway) * headway

best_route = min(routes, key=lambda r: first_departure_after(earliest_departure, r))
best_departure = first_departure_after(earliest_departure, best_route)

print(best_route * (best_departure - earliest_departure))

###

offsets = [(i, int(x)) for i, x in enumerate(inp.split(',')) if x != 'x']

# rest copied directly from
# https://github.com/rf-/advent-of-code-2020/blob/master/day13.rb

t = 0
increment = 1
for offset, v in offsets:
    while (t + offset) % v != 0:
        t += increment
    increment *= v

print(t)
