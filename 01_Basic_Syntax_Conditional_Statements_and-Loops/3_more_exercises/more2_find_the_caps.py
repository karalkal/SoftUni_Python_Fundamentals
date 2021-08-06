word = input()
list_of_chars = list(word)
indexes = []
# cap_letters = list(filter(lambda c: c.isupper(), word))
for i in range(len(word)):
    if "A" <= list_of_chars[i] <= "Z":
        # print(i, end="")
        indexes.append(i)
print(indexes)
