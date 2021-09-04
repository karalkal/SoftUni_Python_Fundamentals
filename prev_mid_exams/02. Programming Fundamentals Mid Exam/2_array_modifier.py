array = [int(x) for x in input().split()]
command = input()

while command != "end":
    if command == "decrease":
        array = [x-1 for x in array]

    else:
        command = command.split()
        action, index1, index2 = command[0], int(command[1]), int(command[2])

        if action == "swap":
            array[index1], array[index2] = array[index2], array[index1]

        elif action == "multiply":
            array[index1] *= array[index2]

    command = input()

print(*array, sep=", ")



