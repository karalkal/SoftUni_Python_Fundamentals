user_entry = input()
initial_list = user_entry.split()
inverted_list = []
# print(initial_list)

for current_num_as_string in range(len(initial_list)):
    if int(initial_list[current_num_as_string]) <= 0:
        opposite_num = abs(int(initial_list[current_num_as_string]))  # makes negatives positive
    elif int(initial_list[current_num_as_string]) > 0:
        opposite_num = -(int(initial_list[current_num_as_string]))
    inverted_list.append(opposite_num)
print(inverted_list)
