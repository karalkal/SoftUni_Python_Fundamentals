original_nums = [int(x) for x in input().split()]
avg = sum(original_nums)/len(original_nums)
new_nums = [x for x in original_nums if x > avg]
if len(new_nums) == 0:
    print("No")
else:
    to_print = []
    new_nums = sorted(new_nums, reverse=True)
    if len(new_nums) <= 5:
        to_print = new_nums
    else:
        for i in range(5):
            to_print.append(new_nums[i])

    print(*to_print)
