text_to_filter = input()
emoticons = []
for i in range(len(text_to_filter)):
    if text_to_filter[i] == ":":
        this_emo = ":" + text_to_filter[i+1]
        emoticons.append(this_emo)

# for sym in text_to_filter:
    # if sym == ":":
    #     emo = ":" + text_to_filter[(text_to_filter.index(sym) + 1)]
    #     emoticons.append(emo)
print(*emoticons, sep="\n")