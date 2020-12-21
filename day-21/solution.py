# TODO: Clean up
from collections import defaultdict

def part1(allergensDict,allIngredients):
    allIngredientsCopy = allIngredients.copy()
    cannots = []

    for allergen in allergensDict:
        cannots.append((allergen,allIngredientsCopy.difference(allergensDict[allergen])))

    cannots.sort(key=lambda x : len(x[1]))
    answers = {}
    done = set()

    while len(done) != len(allergensDict):
        for i in range(len(cannots)-1,-1,-1):
            if i in done:
                continue
            dif = allIngredientsCopy.difference(cannots[i][1])
            if len(dif) > 1:
                continue

            (onlyPossible,) = allIngredientsCopy.difference(cannots[i][1])
            allIngredientsCopy.remove(onlyPossible)
            answers[cannots[i][0]] = onlyPossible
            done.add(i)

    return answers

with open('input-01.txt') as f:
    allergensDict = {}
    allIngredients = set()
    counts = defaultdict(int)

    for line in f.readlines():
        ingredients,allergens = line.split(' (')
        ingredients = ingredients.split(' ')
        allIngredients.update(ingredients)

        for i in ingredients:
            counts[i] += 1

        allergens = allergens[9:].replace(')','').rstrip()
        for allergen in allergens.split(', '):
            if allergen not in allergensDict:
                allergensDict[allergen] = set(ingredients)
            else:
                allergensDict[allergen] = allergensDict[allergen].intersection(set(ingredients))

    allergenToIngredient = part1(allergensDict,allIngredients)

    print(sum(counts[i] for i in allIngredients.difference(set(allergenToIngredient.values()))))    
    print(','.join(allergenToIngredient[allergen] for allergen in sorted(allergenToIngredient.keys())))