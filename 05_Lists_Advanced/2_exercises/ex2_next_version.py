old_version = [int(x) for x in input().split(".")]

if old_version[1] == 9 and old_version[2] == 9 :  # if both are 9
    new_version = str(old_version[0] + 1) + ".0.0"
elif old_version[2] == 9:  # if last is 9
    new_version = str(old_version[0]) + "." + str(old_version[1] + 1) + "." + "0"
else:
    new_version = str(old_version[0]) + "." + str(old_version[1]) + "." + str(old_version[2] + 1)

print(new_version)