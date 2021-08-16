user_input = input().split()
distance = len(user_input) // 2
# print(distance)
a_time = 0
b_time = 0
a_index = 0
b_index = -1
winner = None
winning_time = 0

for _ in range(distance):
    # print(a_index, " ------ ", b_index, sep="")

    if user_input[a_index] == "0":
        a_time *= .8
    else:
        a_time += int(user_input[a_index])

    if user_input[b_index] == "0":
        b_time *= .8
    else:
        b_time += int(user_input[b_index])

    a_index += 1
    b_index -= 1

# print(a_time, "  ", b_time)
if a_time < b_time:
    winner = "left"
    winning_time = f"{a_time:.1f}"
elif b_time < a_time:
    winner = "right"
    winning_time = f"{b_time:.1f}"

print("The winner is {} with total time: {}".format(winner, winning_time))
