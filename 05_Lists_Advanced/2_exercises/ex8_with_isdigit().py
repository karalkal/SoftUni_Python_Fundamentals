original_message_list = input().split()
current_word = ""

for w in original_message_list:
    if w[2].isdigit():
        num_to_break = int(w[:3])
        current_word = chr(num_to_break) + w[3:]
    else:
        num_to_break = int(w[:2])
        current_word = chr(num_to_break) + w[2:]

    if len(current_word) > 2:
        current_word = current_word[:1] + current_word[-1] + current_word[2:-1] + current_word[1]

    print(current_word, end=" ")