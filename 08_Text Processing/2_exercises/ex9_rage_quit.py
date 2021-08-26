user_input = input().upper()
all_values = [x for x in user_input if not x.isdigit()]
unique_chars_len = len(set(all_values))

new = ""
current_position = 0

for i in range(len(user_input)):
    if user_input[i].isdigit():
        if i < len(user_input)-1 and user_input[i + 1].isdigit():  # if num > 9
            repeat = int(user_input[i]) * 10 + int(user_input[i + 1])
        else:
            repeat = int(user_input[i])

        new = new + user_input[current_position:i] * repeat
        current_position = i + 1  # 1 because we want to skip the number as well

print(f"Unique symbols used: {unique_chars_len}")
print(new)
