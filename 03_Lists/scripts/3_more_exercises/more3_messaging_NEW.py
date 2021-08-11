user_input = input().split()
message = input()
result = ""
message_list = []

# split message into list of chars
for letter in message:
    message_list.append(letter)

# for each time there is a number in user input
# 1. transform it into int
# 2. check and change its value according to string length
# 3. remove (pop) relevant char from message
# 4. and add it into result string
for times in user_input:
    index_pick = sum([int(x) for x in times])

    if index_pick > len(message_list) - 1:
        index_pick %= len(message_list)
    letter_pick = message_list.pop(index_pick)
    result += letter_pick
print(result)
