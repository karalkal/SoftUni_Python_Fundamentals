collection = input().split(", ")
command = input()

while command != "Craft!":
    command_as_list = command.split(" - ")
    action, item = command_as_list[0], command_as_list[1]

    if action == "Collect" and item not in collection:
        collection.append(item)

    elif action == "Drop" and item in collection:
        collection.remove(item)

    elif action == "Combine Items":
        combine = item.split(":")
        old = combine[0]

        if old in collection:
            new = combine[1]
            old_index = collection.index(old)
            collection.insert(old_index + 1, new)

    elif action == "Renew" and item in collection:
        collection.remove(item)
        collection.append(item)

    command = input()

print(*collection, sep=", ")
