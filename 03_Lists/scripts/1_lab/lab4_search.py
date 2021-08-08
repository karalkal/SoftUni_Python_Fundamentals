count = int(input())
keyword = input()
list_of_all_entries = []

for _ in range(1, count + 1):
    new_word = input()
    list_of_all_entries.append(new_word)
print(list_of_all_entries)

# it's much easier to just create another list with if keyword in new word.
# this is just an experiment of removing stuff from SAME list
index = 0
while index in range(len(list_of_all_entries)):
    if keyword not in list_of_all_entries[index]:
        list_of_all_entries.pop(index)
        index -= 1
    index += 1
print(list_of_all_entries)

