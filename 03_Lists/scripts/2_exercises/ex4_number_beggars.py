tips_list = input().split(", ")
sequence_of_tips = [int(i) for i in tips_list]
players = int(input())
# print(sequence_of_tips)

final_list = []
for p in range (players):
    final_list.append(0)
# print(final_list)
current_player = 0

for p in range(len(tips_list)):
    current_value = sequence_of_tips[p]
    # print(current_value)
    final_list[current_player] = final_list[current_player] + current_value
    # print(final_list)

    if current_player == players - 1:
        current_player = 0
    else:
        current_player += 1

print(final_list)




