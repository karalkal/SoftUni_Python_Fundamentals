import re
user_input = input()
matches = []
while user_input:
    pattern = r"\d+"
    matches += re.findall(pattern, user_input)
    user_input = input()
print(*matches)