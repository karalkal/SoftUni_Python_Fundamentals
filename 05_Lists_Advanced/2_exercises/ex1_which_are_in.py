list1 = input().split(", ")
list2 = input().split(", ")
new_list = []

for word1 in list1:
    for word2 in list2:
        if word1 in word2:
            new_list.append(word1)
            break
print(new_list)
