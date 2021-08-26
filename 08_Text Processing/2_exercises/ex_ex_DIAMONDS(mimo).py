user_input = input()
allowed_chars = "012345678<>"
diamond_found = False
diamond_value = 0
# filtered_input1 = "".join([x for x in user_input if x in allowed_chars])
filtered_input2 = "".join(filter(lambda a: a in allowed_chars, user_input))
# print(filtered_input1)
# print(filtered_input2)
for i in range(len(filtered_input2)):
    if diamond_found and filtered_input2[i].isdigit():
        diamond_value += int(filtered_input2[i])

    if filtered_input2[i] == "<":
        diamond_found = True
    elif filtered_input2[i] == ">":
        print(f"This diamond's value is {diamond_value}")
        diamond_value = 0
        diamond_found = False

