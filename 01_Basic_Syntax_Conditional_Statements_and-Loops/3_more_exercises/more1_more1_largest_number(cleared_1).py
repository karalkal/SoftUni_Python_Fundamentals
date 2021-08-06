string_num = input()
list_as_strings = []

for i in range(len(string_num)):
    list_as_strings.append(string_num[i])

list_as_strings.sort(reverse=True)
list_as_nums = list(map(int, list_as_strings))

print(*list_as_nums, sep="")
