targets = input().split()
targets = [int(x) for x in targets]
command = input()

while not command == "End":
    command = command.split()
    action, index, power = command[0], int(command[1]), int(command[2])

    if action == "Shoot" and 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.remove(targets[index])

    elif action == "Add":
        if 0 > index or index >= len(targets):
            print("Invalid placement!")
        else:
            targets.insert(index, power)

    elif action == "Strike":
        if index + power >= len(targets) or index - power < 0:
            print("Strike missed!")
        else:
            before = index - power
            after = index + power
            targets = targets[:before] + targets[after + 1:]
    command = input()

print(*targets, sep="|")
