import re

crap_to_filter = input()
pattern = r"\+359([- ])2\1\d{3}\1\d{4}\b"
matches = re.finditer(pattern, crap_to_filter)
phones = [ph.group() for ph in matches]
print(*phones, sep=", ")
