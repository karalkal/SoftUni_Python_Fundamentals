num = int(input())
string_num = str(num)
list_as_strings = []

for i in range(len(string_num)):
    list_as_strings.extend(string_num[i])

list_as_nums = list(map(int, list_as_strings))
list_as_nums.sort(reverse=True)

print(*list_as_nums, sep="")
