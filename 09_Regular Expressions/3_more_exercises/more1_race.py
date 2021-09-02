import re
valid_competitors = input().split(", ")
total_competitors = {}
pattern = r"[A-Za-z0-9]"
while True:
    check_this = input()
    if check_this == "end of race":
        break

    matches = re.findall(pattern, check_this)
    this_competitor = ""
    his_distance = 0
    for match in matches:  # starts again dor each new entered line, all is zero
        if match.isalpha():
            this_competitor += match
        elif match.isdigit:
            his_distance += int(match)

    # check if runner exists in dict
    if this_competitor in total_competitors:
        total_competitors[this_competitor] += his_distance
    else:
        total_competitors[this_competitor] = his_distance

# print(total_competitors)
filtered_dict = {k: v for (k, v) in total_competitors.items() if k in valid_competitors}
# print(filtered_dict)
sorted_list = sorted(filtered_dict.items(), key=lambda x: -x[1])
# print(sorted_list)
print(f"1st place: {sorted_list[0][0]}")
print(f"2nd place: {sorted_list[1][0]}")
print(f"3rd place: {sorted_list[2][0]}")