original = [int(x) for x in input().split(", ")]
upper_limit = max(original) // 10 + 1
if max(original) % 10 == 0:
    upper_limit -= 1
for i in range(1, upper_limit + 1):
    current_list = [x for x in original if (i - 1) * 10 < x <= i * 10]
    print(f"Group of {i}0's: {current_list}")
