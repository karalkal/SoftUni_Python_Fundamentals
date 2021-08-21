contests_dict = {}
while True:
    contest = input()
    if contest == "end of contests":
        break

    contest = contest.split(":")
    key = contest[0]
    value = contest[1]
    contests_dict[key] = {"Pass": value}  # contest:password

    users_results = {}
while True:
    submission = input()
    if submission == "end of submissions":
        break

    submission = submission.split("=>")
    contest, password, username, points = submission[0], submission[1], submission[2], int(submission[3])

    # if no such contest or password doesn't match -> Try again
    if contest not in contests_dict or password != contests_dict[contest]["Pass"]:
        # print("ebi si majkata")
        continue

    # if contest is valid and password matches
    # create user with this name and get ready for contests: points
    if username not in users_results.keys():
        users_results[username] = {contest: points}

    else:
        if contest not in users_results[username].keys():  # if user hasn't submitted previously
            users_results[username][contest] = points
        else:
            current_best_points = users_results[username][contest]
            if current_best_points < points:
                users_results[username][contest] = points

best_result = -1
best_student = None
for k, v in users_results.items():
    list_of_persons_results = [int(x) for x in v.values()]
    if sum(list_of_persons_results) > best_result:
        best_result = sum(list_of_persons_results)
        best_student = k  # the student with current best value is number one
print(f"Best candidate is {best_student} with total {best_result} points.")

users_sorted_alphabetically = dict(sorted(users_results.items(), key=lambda x: x[0]))
print("Ranking:")
for k1, val_dict in users_sorted_alphabetically.items():
    print(k1)

    # sort their results, descending
    sorted_users_results = dict(sorted(val_dict.items(), key=lambda x: -x[1]))
    for k, v in sorted_users_results.items():
        print(f"#  {k} -> {v}")


