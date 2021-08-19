how_many = int(input())
words_and_synonyms = {}
for i in range(how_many):
    word = input()
    synonym = input()
    if word in words_and_synonyms:
        words_and_synonyms[word] += ", " + synonym
    else:
        words_and_synonyms[word] = synonym

for (word, synonym) in words_and_synonyms.items():
    print(f"{word} - {synonym}")

# print(words_and_synonyms)
