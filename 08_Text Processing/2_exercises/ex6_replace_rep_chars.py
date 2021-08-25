original = input()
new_str = ""
current_letter = ""
for letter in original:
    if letter != current_letter:
        current_letter = letter
        new_str += letter
print(new_str)
