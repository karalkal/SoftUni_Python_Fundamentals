import re
text_to_filter = input()

pattern = r"\b(?P<date>\d\d)(?P<sep>[/.-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>[0-9]{4})"

# kur = re.compile(r"\b(?P<date>\d\d)(?P<sep>[/.-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>[0-9]{4})")
# oppa = kur.findall(text_to_filter)
# print(oppa)
# THESE TWO ARE EQUIVALENT
oppa1 = re.findall(pattern, text_to_filter)
for vd in range(len(oppa1)):
    print(f"Day: {oppa1[vd][0]}, Month: {oppa1[vd][2]}, Year: {oppa1[vd][3]}")

# matches = re.finditer(pattern, text_to_filter)
# for valid_date in matches:
#     print(f"Day: {valid_date.group(1)}, Month: {valid_date.group(3)}, Year: {valid_date.group(4)}")
