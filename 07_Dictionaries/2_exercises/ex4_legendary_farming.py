all_items = {}
not_collected = True

while not_collected:
    list_user_input = [x.lower() for x in input().split()]

    for i in range(1, len(list_user_input), 2):
        key = list_user_input[i]
        value = int(list_user_input[i - 1])

        if key in all_items.keys():
            all_items[key] += value
        else:
            all_items[key] = value

        if "shards" in all_items.keys() and all_items["shards"] >= 250:
            print("Shadowmourne obtained!")
            all_items["shards"] -= 250
            not_collected = False
            break

        if "fragments" in all_items.keys() and all_items["fragments"] >= 250:
            print("Valanyr obtained!")
            all_items["fragments"] -= 250
            not_collected = False
            break

        if "motes" in all_items.keys() and all_items["motes"] >= 250:
            print("Dragonwrath obtained!")
            all_items["motes"] -= 250
            not_collected = False
            break

# sorts entries by KEY, therefore adding items one by one, in this case alphabetical order
# sorted_all = {}
# for i in sorted(all_items):
#     sorted_all[i] = all_items[i]
sorted_all = {k: v for (k, v) in sorted(all_items.items())}  # same as above

# new dictionaries for important and crap materials
important_materials = {"fragments": 0, "motes": 0, "shards": 0}
crap_materials = {}

for key, value in sorted_all.items():
    if key == "shards" or key == "fragments" or key == "motes":
        important_materials[key] = value
        # sorted_important = sorted(important_materials.values(), reverse=True)
        sorted_important = dict(
            sorted(important_materials.items(), key=lambda x: x[1], reverse=True))
        # sorted RETURNS LIST of tuples! Therefore x[1] is second value in each pairs

    else:
        crap_materials[key] = value

# print(sorted_important)

for key, value in sorted_important.items():
    print(key + ": " + str(value))
for key, value in crap_materials.items():
    print(key + ": " + str(value))
