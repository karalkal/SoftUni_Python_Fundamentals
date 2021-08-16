items_to_buy = input().split()
command = input()

while command != "No Money":
    command_as_list = command.split()

    if command_as_list[0] == "OutOfStock" and command_as_list[1] in items_to_buy: # if there are any
        # change their values to "None"
        for i in range(len(items_to_buy)):
            if items_to_buy[i] == command_as_list[1]:  # finds the string
                items_to_buy[i] = None  # puts value None

    if command_as_list[0] == "Required":
        # Replace the value of the current gift on the given index with this gift if the index is valid
        index_of_required = int(command_as_list[2])
        index_of_removed = index_of_required - 1
        if index_of_required > len(items_to_buy): # if the index is valid
            continue
        elif index_of_required == len(items_to_buy):  # if index is same as last element
            items_to_buy.append(command_as_list[1])
        else:
            items_to_buy[index_of_required] = command_as_list[1]

    if command_as_list[0] == "JustInCase":
        items_to_buy[-1] = command_as_list[1]

    command = input()

final_list =  [item for item in items_to_buy if item] #res = [i for i in test_list if i]
print(*final_list, sep=" ")
