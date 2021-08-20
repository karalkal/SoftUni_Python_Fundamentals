command = input()
teams = {}
user_exists = False
while command != "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")
        # it user exists do nothing
        for v_list in teams.values():
            if user in v_list:
                user_exists = True
                break
            else:
                user_exists = False

        if not user_exists:
            if side not in teams.keys():
                teams[side] = [user]
            else:
                teams[side] += [user]
        # otherwise skip

    elif "->" in command:
        user, side = command.split(" -> ")
        # First check if guy exists and remove him
        for v_list in teams.values():
            if user in v_list:
                v_list.remove(user)
                break
        if side in teams:
            teams[side] += [user]
        else:
            teams[side] = [user]

        print(f"{user} joins the {side} side!")

    command = input()
cleared_teams = {k: sorted(v) for (k, v) in teams.items() if len(v) > 0}
# print(teams)
# print(cleared_teams)
sorted_dict = dict(sorted(cleared_teams.items(), key=lambda x: (-len(x[1]), x[0])))
# print(sorted_dict)
for key, value in sorted_dict.items():
    print(f"Side: {key}, Members: {len(value)}")
    print("!", "\n! ".join(value))