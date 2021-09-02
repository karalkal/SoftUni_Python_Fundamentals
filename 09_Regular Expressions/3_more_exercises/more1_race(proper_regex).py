import re

pattern = r"(?P<letters>[A-Za-z])|(?P<digits>[0-9])"
valid_competitors = input().split(", ")
valid_competitors = {k: 0 for k in valid_competitors}
while True:
    check_this = input()
    if check_this == "end of race":
        break

    matches = re.finditer(pattern, check_this)

    # here we filter all letters -> names and all digits - > distance
    this_runner, his_distance = "", 0
    for match in matches:
        if match.group("letters"):
            this_runner += match.group("letters")
        if match.group("digits"):
            his_distance += int(match.group("digits"))

    # then we check if runner is in initial list
    if this_runner in valid_competitors:
        valid_competitors[this_runner] += his_distance
winners_dict = sorted(valid_competitors.items(), key=lambda x: -x[1])
print(f"1st place: {winners_dict[0][0]}")
print(f"2nd place: {winners_dict[1][0]}")
print(f"3rd place: {winners_dict[2][0]}")
