string_to_check = input().split(", ")
valid = []
for checked in string_to_check:
    if 3 < len(checked) < 16 and (checked.isalnum() \
                                  or "_" in checked \
                                  or "-" in checked):
        valid.append(checked)
print(*valid, sep="\n")
