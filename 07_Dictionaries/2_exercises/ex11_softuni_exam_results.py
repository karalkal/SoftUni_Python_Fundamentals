command = input()
dict_results = {}
dict_language = {}
while command != "exam finished":
    result = command.split("-")
    if result[1] != "banned":
        name, language, mark = result[0], result[1], int(result[2])

        if language not in dict_language:
            dict_language[language] = 1
        else:
            dict_language[language] += 1

        if name not in dict_results:
            dict_results[name] = mark
        elif dict_results[name] < mark:
            dict_results[name] = mark

    else:  # banned
        banned_user = result[0]
        del dict_results[banned_user]
    command = input()

# print(dict_results)
# print(dict_language)

sorted_dict_results = dict(sorted(dict_results.items(), key=lambda x: (-x[1], x[0])))  # by HIGHEST mark, then by name
sorted_dict_language = dict(sorted(dict_language.items(), key=lambda x: (-x[1], x[0])))  # by MOST participants, then by lang. name
# print(sorted_dict_results)
print("Results:")
for k, v in sorted_dict_results.items():
    print(f"{k} | {v}")

print("Submissions:")
for k, v in sorted_dict_language.items():
    print(f"{k} - {v}")
