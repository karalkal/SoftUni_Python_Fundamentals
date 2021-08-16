train = [0] * int(input())
command = input()

while command != "End":
    command = command.split()
    action, num1 = command[0], int(command[1])

    if action == "add":
        train[-1] += num1
    else:
        num2 = int(command[2])

    if action == "insert":
        train[num1] = train[num1] + num2
    elif action == "leave":
        train[num1] = train[num1] - num2

    command = input()
print(train)
