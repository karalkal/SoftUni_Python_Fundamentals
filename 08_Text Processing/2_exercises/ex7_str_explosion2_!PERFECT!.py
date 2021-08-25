original = input()
new = ""
power = 0
will_skip = False

for i in range(len(original)):
    current_char = original[i]

    if current_char == ">":
        will_skip = True
        power += int(original[i+1])
        new += ">"
        continue
    if will_skip:
        new += ""
        power -= 1
        if power == 0:
            will_skip = False
    else:
        new += current_char

print(new)
