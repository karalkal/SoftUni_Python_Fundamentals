count = int(input())
keyword = input()
list_of_all_entries = []
filtered_list = []

for _ in range(1, count + 1):
    new_word = input()
    list_of_all_entries.append(new_word)
    if keyword in new_word:
        filtered_list.append(new_word)

print(list_of_all_entries)
print(filtered_list)
