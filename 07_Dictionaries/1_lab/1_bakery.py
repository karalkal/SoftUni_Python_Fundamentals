ingredients = input().split()
bakery = {}
for i in range(0, len(ingredients), 2):
    key = ingredients[i]
    value = ingredients[i + 1]
    bakery[key] = int(value)
print(bakery)

