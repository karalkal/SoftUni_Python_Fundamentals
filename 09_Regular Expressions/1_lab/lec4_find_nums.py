import re

text_to_filter=input()
pattern = r"(^|(?<=\s))\-?[0-9]+(\.?[0-9]*)($|(?=\s))"
found = re.finditer(pattern, text_to_filter)
for n in found:
    print(n.group(), end=" ")
