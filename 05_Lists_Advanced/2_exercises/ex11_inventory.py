items = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")

    if command[0] == "Drop" and command[1] in items:
        items.remove(command[1])

    # This is a test as the task is obv wrong
    elif command[0] == "Collect" and command[1] not in items:
        items.append(command[1])

    elif command[0] == "Renew" and command[1] in items:
        items.append(command[1])
        items.remove(command[1])

    elif command[0] == "Combine Items":
        combine = command[1].split(":")
        if combine[0] in items:
            to_put_after = items.index(combine[0])
            if to_put_after >= len(items):
                items.append(combine[1])
            else:
                items.insert(to_put_after + 1, combine[1])

    command = input()

print(*items, sep=", ")
