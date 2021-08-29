import re
text_to_filter = input()

pattern = r"\b(?P<date>\d\d)(?P<sep>[/.-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>[0-9]{4})"

matches = re.finditer(pattern, text_to_filter)
for valid_date in matches:
    print(f"Day: {valid_date.group(1)}, Month: {valid_date.group(3)}, Year: {valid_date.group(4)}")
