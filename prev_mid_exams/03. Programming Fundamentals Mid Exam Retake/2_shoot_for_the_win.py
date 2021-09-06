targets = input().split()
targets = [int(x) for x in targets]
current_index = input()
count = 0

while current_index != "End":
    current_index = int(current_index)

    if current_index < len(targets) and targets[current_index] != -1:
        value = targets[current_index]
        targets[current_index] = -1
        count += 1


        for i in range(len(targets)):
            if targets[i] > value and targets[i] != -1:
                targets[i] -= value
            elif targets[i] <= value and targets[i] != -1:
                targets[i] += value

    current_index = input()
print(f"Shot targets: {count} -> ", end="")
print(*targets, sep=" ")