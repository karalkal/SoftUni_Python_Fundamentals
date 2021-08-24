unencrypted = input()
encrypted = ""
for letter in unencrypted:
    encrypted += chr(ord(letter) + 3)
print(encrypted)