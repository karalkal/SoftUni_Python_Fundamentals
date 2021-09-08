groceries = input().split("!")
command = input()

while command != "Go Shopping!":
    current_entry = command.split()
    adj = current_entry[0]
    stuff = current_entry[1]

    if adj == "Urgent" and stuff not in groceries:
        groceries.insert(0, stuff)
    elif adj == "Unnecessary" and stuff in groceries:
        groceries.remove(stuff)
    elif adj == "Correct" and stuff in groceries:
        replace_with = current_entry[2]
        index_of_removed = groceries.index(stuff)
        groceries.pop(index_of_removed)
        groceries.insert(index_of_removed, replace_with)
    elif adj == "Rearrange" and stuff in groceries:
        groceries.append(stuff)
        groceries.remove(stuff)

    command = input()

print(*groceries, sep=", ")
# kur = ", ".join(groceries)
# print(kur)