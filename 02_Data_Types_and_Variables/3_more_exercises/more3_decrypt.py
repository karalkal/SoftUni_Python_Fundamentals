key = int(input())
lines = int(input())
for l in range(1, lines + 1):
    user_letter = ord(input())
    deciphered_letter = user_letter + key
    print(chr(deciphered_letter), end="")
