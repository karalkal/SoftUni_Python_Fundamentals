user_input = input().split()
count = int(input())
number_of_cards = len(user_input)

for c in range(count):
    first_half_list = []
    for i in range(number_of_cards // 2):
        card_of_first_half = user_input.pop(0)
        first_half_list.append(card_of_first_half)

    second_half_list = user_input  # now user input is trimmed to second half items

    new_list = []

    for new_card in range(number_of_cards // 2):
        new_list.append(first_half_list[new_card])
        new_list.append(second_half_list[new_card])

        user_input = new_list  # replacing the user input for the next iteration

print(new_list)



