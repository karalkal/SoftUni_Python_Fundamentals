input_as_string = input()
nums_list_as_string = []
sentence = input()
result = ""

for i in range(len(input_as_string)):
    if input_as_string[i] != " ":
        nums_list_as_string.append(input_as_string[i])
nums_list_as_digits = [int(x) for x in nums_list_as_string]
our_num = sum(nums_list_as_digits)

if our_num + 1 > len(sentence):
    our_num = our_num % len(sentence)
print(sentence[our_num])