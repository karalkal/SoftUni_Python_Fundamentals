list_of_codes = input().split()
result = 0
for instance in list_of_codes:
    # last_char_position = len(instance) - 1
    first_letter = instance[0]
    last_letter = instance[-1]
    num = int(instance[1:-1])

    if first_letter.isupper():
        num = num / (ord(first_letter) - 64)
    else:
        num = num * (ord(first_letter) - 96)

    if last_letter.isupper():
        num -= (ord(last_letter) - 64)
    else:
        num += (ord(last_letter) - 96)

    result += num
print(f"{result:.2f}")
