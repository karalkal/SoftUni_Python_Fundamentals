num = int(input())
string_num = str(num)
numbers_store = []
for i in range(len(string_num)):
    # print(string_num[i])
    numbers_store.extend(string_num[i])
# Does NOT change the order in the list
# print(sorted(numbers_store))
# print(numbers_store)
# print()

# DOES change the order in the list
numbers_store.sort(reverse=True)
# print(numbers_store)

list2 = list(map(int, numbers_store))
print(*list2, sep="")
