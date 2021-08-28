import re
name_to_check = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
check = re.findall(pattern, name_to_check)
print(*check)