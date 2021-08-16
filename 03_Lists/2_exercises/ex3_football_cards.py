a_team = []
b_team = []
for player_no in range(1, 12):
    a_current_player = "A-" + str(player_no)
    a_team.append(a_current_player)
    b_current_player = "B-" + str(player_no)
    b_team.append(b_current_player)
# print(a_team)
# print(b_team)

game_is_terminated = False

user_input = input()
list_of_cards = user_input.split()
# print(list_of_cards)
for player_sent_off in range(len(list_of_cards)):
    # print(list_of_cards[card])
    if list_of_cards[player_sent_off] in a_team:
        a_team.remove(list_of_cards[player_sent_off])
    if list_of_cards[player_sent_off] in b_team:
        b_team.remove(list_of_cards[player_sent_off])

    if len(a_team) < 7 or len(b_team) < 7:
        game_is_terminated = True
        break


print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if game_is_terminated:
    print("Game was terminated")
