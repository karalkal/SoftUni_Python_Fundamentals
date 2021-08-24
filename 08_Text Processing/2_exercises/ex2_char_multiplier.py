one, two = input().split(" ")
result = 0
if len(one) ==len(two):
    for letter in range(len(two)):
        result += ord(one[letter]) * ord(two[letter])

elif len(one) < len(two):
    difference_in_len = len(two) - len(one)
    for letter in range(len(one)):
        result += ord(one[letter]) * ord(two[letter])
    for remaining in range(len(one), len(two)):
        result += ord(two[remaining])

else:
    difference_in_len = len(one) - len(two)
    for letter in range(len(two)):
        result += ord(one[letter]) * ord(two[letter])
    for remaining in range(len(two), len(one)):
        result += ord(one[remaining])


print(result)
