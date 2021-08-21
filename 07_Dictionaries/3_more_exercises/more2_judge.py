all_contests = {}

while True:
    user_input = input().split(" -> ")
    if user_input[0] == "no more time":
        break

    username, contest, points = user_input[0], user_input[1], int(user_input[2])

    # if new contest
    if contest not in all_contests:
        all_contests[contest] = {username: points}
    else:
        # if existing contest but new user
        if username not in all_contests[contest].keys():
            all_contests[contest][username] = points
        # if user exists check if new points score is higher
        else:
            if all_contests[contest][username] < points:
                all_contests[contest][username] = points

# standings by contest
for k, values_dict in all_contests.items():
    print(f"{k}: {len(values_dict)} participants")
    sorted_values = dict(sorted(values_dict.items(), key=lambda x: (-x[1], x[0])))
    rank = 0
    for k, v in sorted_values.items():
        rank += 1
        print(f"{rank}. {k} <::> {v}")

# individual standings
individual = {}
for player in all_contests.values():
    for k, v in player.items():
        if k not in individual:
            individual[k] = v
        else:
            individual[k] += v
sorted_individual = dict(sorted(individual.items(), key=lambda x: (-x[1], x[0])))
print("Individual standings:")
rank = 0
for k, v in sorted_individual.items():
    rank += 1
    print(f"{rank}. {k} -> {v}")
