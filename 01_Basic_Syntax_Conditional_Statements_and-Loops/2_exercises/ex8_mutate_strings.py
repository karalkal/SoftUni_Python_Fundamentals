word1 = input()
word2 = input()

for letter in range(0, len(word2)):
    # print(w1[letter])
    # print(w2[letter])
    if word2[letter] != word1[letter]:
        word1 = word1[0:letter] + word2[letter] + word1[letter + 1:]
        print(word1)
