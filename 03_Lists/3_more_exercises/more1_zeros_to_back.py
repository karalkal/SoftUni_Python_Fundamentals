original_list = input().split(", ")
list_as_nums = [int(el) for el in original_list]  # transform to digits

for i in range(len(list_as_nums)):
    current_num = list_as_nums[i]

    if current_num == 0:
        list_as_nums.remove(0)
        list_as_nums.append(0)

print(list_as_nums)