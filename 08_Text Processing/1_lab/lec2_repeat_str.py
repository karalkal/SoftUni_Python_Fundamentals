words = input().split()
for i in range(len(words)):
    this_words_len = len(words[i])
    print(words[i] * this_words_len, end="")
