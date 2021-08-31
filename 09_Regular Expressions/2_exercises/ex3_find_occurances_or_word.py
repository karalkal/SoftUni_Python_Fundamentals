import re
text_to_filter = input().lower()
word_to_count = input().lower()
pattern = r"\b" + word_to_count + r"\b"
matches = re.findall(pattern, text_to_filter)
print(len(matches))