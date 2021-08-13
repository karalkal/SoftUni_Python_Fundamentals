import math

stringed_input = input().split(" ")
numbers_list = [int(x) for x in stringed_input]

command = input()

while command != "end":
    list_command = command.split()  # split only if != "end"
    value1 = list_command[0]
    value2 = list_command[1]

    # case "exchange
    if value1 == "exchange":
        value2 = int(value2)
        if value2 < 0 or value2 > len(numbers_list) - 1:
            print("Invalid index")
        else:
            for i in range(0, value2 + 1):
                # x = num_input_list.pop(0)
                # num_input_list.append(x)
                # same as above 2 lines
                numbers_list.append(numbers_list.pop(0))

    # case max even/odd
    if value1 == "max":
        max_num = -math.inf  # second command is even
        if value2 == "even":
            for i in range(len(numbers_list)):
                if numbers_list[i] >= max_num and numbers_list[i] % 2 == 0:
                    # = sign is to overwrite if same value is found right from current
                    max_num = numbers_list[i]
                    winning_index = i
        # second command is odd
        elif value2 == "odd":
            for i in range(len(numbers_list)):
                if numbers_list[i] >= max_num and numbers_list[i] % 2 == 1:
                    # = sign is to overwrite if same value is found right from current
                    max_num = numbers_list[i]
                    winning_index = i

        if max_num == -math.inf:
            print("No matches")
        else:
            print(winning_index)

        # case min even/odd
    if value1 == "min":
        min_num = math.inf  # second command is even
        if value2 == "even":
            for i in range(len(numbers_list)):
                if numbers_list[i] <= min_num and numbers_list[i] % 2 == 0:
                    # = sign is to overwrite if same value is found right from current
                    min_num = numbers_list[i]
                    winning_index = i
        # second command is odd
        elif value2 == "odd":
            for i in range(len(numbers_list)):
                if numbers_list[i] <= min_num and numbers_list[i] % 2 == 1:
                    # = sign is to overwrite if same value is found right from current
                    min_num = numbers_list[i]
                    winning_index = i

        if min_num == math.inf:
            print("No matches")
        else:
            print(winning_index)

    # case first {count} even/odd
    if value1 == "first":
        value2 = int(value2)  # how many numbers to pick

        if value2 > len(numbers_list):
            print("Invalid count")

        else:
            value3 = list_command[2]  # odd or even
            new_list = []  # to append with valid nums
            if value3 == "even":
                for i in range(len(numbers_list)):
                    if numbers_list[i] % 2 == 0:
                        new_list.append(numbers_list[i])
                        if len(new_list) == value2:
                            break

            elif value3 == "odd":
                for i in range(len(numbers_list)):
                    if numbers_list[i] % 2 == 1:
                        new_list.append(numbers_list[i])
                        if len(new_list) == value2:
                            break

            print(new_list)


    # case last {count} even/odd
    if value1 == "last":
        value2 = int(value2)  # how many numbers to pick

        if value2 > len(numbers_list):
            print("Invalid count")

        else:
            value3 = list_command[2]  # odd or even
            new_list = []  # to append with valid nums
            if value3 == "even":
                for i in range(len(numbers_list) - 1, -1, -1):
                    if numbers_list[i] % 2 == 0:
                        new_list.insert(0, numbers_list[i])  # append(numbers_list[i])
                        if len(new_list) == value2:
                            break

            elif value3 == "odd":
                for i in range(len(numbers_list) - 1, -1, -1):
                    if numbers_list[i] % 2 == 1:
                        new_list.insert(0, numbers_list[i])  # append(numbers_list[i])
                        if len(new_list) == value2:
                            break

            print(new_list)

    command = input()

print(numbers_list)
