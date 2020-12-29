import re
from collections import defaultdict
from functools import reduce

all_ingredients = set()
counts = defaultdict(int)
candidates = {}

with open('inputs/21') as f:
    for line in f:
        ingredient_list, allergen_list = re.match(r'^(.+) \(contains (.+)\)$',
                                                  line.strip()).groups()
        ingredients = ingredient_list.split(' ')
        allergens = allergen_list.split(', ')
        all_ingredients.update(ingredients)
        for a in allergens:
            if a not in candidates:
                candidates[a] = set(ingredients)
            else:
                candidates[a] &= set(ingredients)
        for i in ingredients:
            counts[i] += 1

def possible_combinations(candidates, combos=None):
    combos = None
    for allergen, ingredients in candidates.items():
        if combos is None:
            combos = [{ i: allergen } for i in ingredients]
        else:
            combos = [dict({ i: allergen }, **combo)
                      for combo in combos
                      for i in ingredients
                      if i not in combo]
    return combos

# part 1
possible_ingredients = reduce(set.union, map(set, possible_combinations(candidates)))
impossible_ingredients = all_ingredients ^ possible_ingredients
print(sum(counts[i] for i in impossible_ingredients))

# part 2
print(','.join(ingredient
               for ingredient, _ in
               sorted(possible_combinations(candidates)[0].items(),
                      key=lambda pair: pair[1])))
