gifts_list = input().split()
num_of_items = len(gifts_list)
neg_len = -num_of_items
command = input()

while command != "No Money":
    split_command = command.split()

    action = split_command[0]
    value = split_command[1]
    if action == "Required":    # if "Required" we need the third entry [index2] as num
        index_to_replace = int(split_command[2])

    if action == "OutOfStock" and value in gifts_list:  # if there are any
        for i in range(num_of_items):
            if gifts_list[i] == value:
                gifts_list[i] = None
    elif action == "Required" and neg_len <= index_to_replace < num_of_items:  # must be less as index in minus 1
        gifts_list[index_to_replace] = value

    elif action == "JustInCase":
        gifts_list[-1] = value

    command = input()

num_of_items = len(gifts_list)
# print(gifts_list)
for r in range(num_of_items):
    if gifts_list[r]:  # if exists, i.e. not None
        print(gifts_list[r], end=" ")