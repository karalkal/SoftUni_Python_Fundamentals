ingredients = input().split()
keys_bakery = []
values_bakery = []
for i in range(len(ingredients)):
    if i % 2 == 0:
        keys_bakery.append(ingredients[i])
    else:
        values_bakery.append(int(ingredients[i]))
bakery = {}
for i in range(len(keys_bakery)):
    bakery[keys_bakery[i]] = values_bakery[i]

print(bakery)
