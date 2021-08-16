targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command = command.split()
    action, index, value = command[0], int(command[1]), int(command[2])

    if action == "Shoot" and 0 <= index < len(targets):
        targets[index] = targets[index] - value
        if targets[index] <=0:
            targets.pop(index)

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if 0 <= index - value and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")
    command = input()
print(*targets, sep="|")