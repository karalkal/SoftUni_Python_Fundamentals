loot = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        items_to_add = command[1:]
        for item in items_to_add:
            if item not in loot:
                loot.insert(0, item)

    elif action == "Drop":
        index = int(command[1])
        if 0 <= index < len(loot):  # if is valid
            dropped_item = loot.pop(index)
            loot.append(dropped_item)

    elif action == "Steal":
        stolen_count = int(command[1])
        if stolen_count >= len(loot):
            print(", ".join(loot))
            loot = []
        else:
            stolen_items = []
            to_remain = len(loot) - stolen_count
            stolen_items = loot[to_remain:]
            print(", ".join(stolen_items))
            loot = loot[:to_remain]
    command = input()

if len(loot) == 0:
    print("Failed treasure hunt.")
else:
    sum_of_items = 0
    for item in loot:
        sum_of_items += len(item)
    gain = f"{sum_of_items / len(loot):.2f}"
    print(f"Average treasure gain: {gain} pirate credits.")
