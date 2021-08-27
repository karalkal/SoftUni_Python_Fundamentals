start = ord(input())
end = ord(input())

text_to_filter = input()
sum_of_ascii_codes = 0
# found_chars = []

for char in text_to_filter:
    if start < ord(char) < end:
        # found_chars.append(char)
        sum_of_ascii_codes += ord(char)
print(sum_of_ascii_codes)