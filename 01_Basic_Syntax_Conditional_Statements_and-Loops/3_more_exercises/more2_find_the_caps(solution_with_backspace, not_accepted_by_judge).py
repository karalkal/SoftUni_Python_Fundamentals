word = input()
print("[", end="")
for i in range(len(word)):
    if word[i] in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        # print(word[i], end="")  prints capital letters
        print(i, end=", ")
print("\b\b]", end="")

