notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0])
    note = tokens[1]
    if priority == 10:
        notes.append(note)

    notes.pop(priority)
    notes.insert(priority, note)

new_list = [x for x in notes if x != 0]
print(new_list)




