user_input = input()
list_chars = [x for x in user_input if x != " "]
dict_chars = {}

for key in list_chars:
    if key in dict_chars:
        dict_chars[key] += 1
    else:
        dict_chars[key] = 1

# print(dict_chars)
for (key, value) in dict_chars.items():
    print(key, "->", value)
