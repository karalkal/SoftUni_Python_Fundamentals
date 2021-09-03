targets = [x for x in input().split()]
command = input()
moves = 0
won = False
while command != "end":
    moves += 1
    shot = [int(x) for x in command.split()]
    i1, i2 = shot[0], shot[1]
    if shot[0] == shot[1] or shot[0] < 0 or shot[1] < 0 \
            or shot[0] >= len(targets) or shot[1] >= len(targets):
        print("Invalid input! Adding additional elements to the board")
        targets.insert(len(targets) // 2, str(-moves) + "a")
        targets.insert(len(targets) // 2, str(-moves) + "a")

    elif targets[i1] == targets[i2]:
        print(f"Congrats! You have found matching elements - {targets[i1]}!")

        if i1 > i2:
            targets.remove(targets[i2])
            targets.remove(targets[i1-1])
        else:
            targets.remove(targets[i1])
            targets.remove(targets[i2 - 1])

    else:
        print("Try again!")

    if len(targets) <= 0:
        won = True
        break

    command = input()
if won:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(*targets, sep=" ")
