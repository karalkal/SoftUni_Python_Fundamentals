st_user_nums = input().split()
int_user_nums = [int(element) for element in st_user_nums]

nums_to_remove = int(input())
nums_to_remain = len(int_user_nums) - nums_to_remove

list_of_largest_nums = []

for large_nums in range(nums_to_remain):
    # max_num = int_user_nums.pop(max(int_user_nums))
    list_of_largest_nums.append(max(int_user_nums))
    int_user_nums.remove(max(int_user_nums))

print(list_of_largest_nums)
