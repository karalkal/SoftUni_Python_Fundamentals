original = input()
all_chars = [x for x in original]

vowels1 = ["a", "e", "o", "u", "i"]
vowels2 = [x.upper() for x in vowels1]
vowels = vowels1 + vowels2
filtered_chars = [x for x in all_chars if x not in vowels]
print(*filtered_chars, sep="")