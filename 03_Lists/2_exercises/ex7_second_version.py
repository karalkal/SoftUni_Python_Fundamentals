items_to_buy = input().split()
command = input()

while command != "No Money":
    command_as_list = command.split()
    what_to_do = command_as_list[0]
    new_item = command_as_list[1]

    if what_to_do == "OutOfStock" and new_item in items_to_buy:  # if there are any
        # change their values to "None"
        for i in range(len(items_to_buy)):
            if items_to_buy[i] == new_item:  # finds the string
                items_to_buy[i] = None  # puts value None to corresponding index

    elif what_to_do == "Required":
        # Replace the value of the current gift on the given index with this gift if the index is valid
        index_of_required = int(command_as_list[2])
        if index_of_required < len(items_to_buy):
            items_to_buy[index_of_required] = new_item  # replaces current item in position with the new item
        # if index_of_required == len(items_to_buy):  # if index is same as last element -> add to list
        #     items_to_buy.append(new_item)

    elif what_to_do == "JustInCase":
        items_to_buy[-1] = new_item  # replaces last item

    command = input()

final_list = [item for item in items_to_buy if item]
print(*final_list, sep=" ")
