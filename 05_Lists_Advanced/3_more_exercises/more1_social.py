original_list = [int(x) for x in input().split(", ")]
threshold = int(input())
poor_list = []
rich_list = []
not_poor_anymore=[]

if sum(original_list) < len(original_list) * threshold:
    print("No equal distribution possible")

else:
    for p in original_list:
        if p < threshold:
            poor_list.append(p)
        else:
            rich_list.append(p)

    while len(poor_list) > 0:
        lowest_value = poor_list.pop(poor_list.index(min(poor_list)))
        not_poor_anymore.append(threshold)

        deduct_by = threshold - lowest_value

        richest_man = rich_list.index(max(rich_list))
        rich_list[richest_man] -= deduct_by

    print(not_poor_anymore + rich_list)

