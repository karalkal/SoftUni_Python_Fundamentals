initial = list(input())
nums1 = []
letters = []
take = []
skip = []
result = []
t = 0
for i in range(len(initial)):
    if initial[i].isnumeric():
        nums1.append(int(initial[i]))
    else:
        letters.append(initial[i])

for j in range(len(nums1)):
    if j % 2 == 0:
        take.append(nums1[j])
    else:
        skip.append(nums1[j])

for l in range(len(take)):
    # print(f"take this: {value_of_take} - skip this: {value_of_skip}")

    for t in range(take[l]):
        result.append(letters[0])
        letters.pop(0)

    for s in range(skip[l]):
        if len(letters) == 0:
            break
        letters.pop(0)

print(*result, sep="")


#
# result += letters[:take[0]]
# print(*result, sep="")
#
# next_portion = letters[len(result) + skip[0]:take[1]]
# result += next_portion
# print(*result, sep="")
#
# next_portion = letters[len(result) + skip[1]:take[2]]
# result += next_portion
# print(*result, sep="")
#
# # next_start = len(result) + skip[0]
# # up_to = next_start + take[1]
# # result += letters[next_start:up_to]
# print(*result, sep="")