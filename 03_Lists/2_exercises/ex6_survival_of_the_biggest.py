st_user_nums = input().split()
int_user_nums = [int(element) for element in st_user_nums]

nums_to_remove = int(input())

for num1 in range(1, nums_to_remove + 1):
    int_user_nums.remove(min(int_user_nums))

# if you put the asterisk in front of your iterable this decomposes it into
# separate arguments and allows for the intended use of sep
print(*int_user_nums, sep=", ")
