user_input = [x.lower() for x in input().split()]
occurrences = {}
final = []

for i in range(len(user_input)):
    key = user_input[i]
    value = 1
    if key in occurrences:
        occurrences[key] += value
    else:
        occurrences[key] = value

for (key, value) in occurrences.items():
    if value % 2 == 1:
        print(key, end=" ")
