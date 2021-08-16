input_as_string = input().split()
sentence = input()
result = ""

for i in range(len(input_as_string)):
    current_num_as_string = list(input_as_string[i])
    our_number = sum([int(x) for x in current_num_as_string])
    # print(our_number)

    if our_number + 1 > len(sentence):
        our_number = our_number % len(sentence)

    result += sentence[our_number]

    sentence = sentence[:our_number] + sentence[our_number+1:]

print(result)
