import re
text_to_filter = input()
pattern = r"(^|(?<=\s))[a-z0-9]+[\._-]*[a-z0-9]+@[a-z]+\-*[a-z]+\.[a-z]+\-*[a-z]+(\.[a-z]+\-*[a-z]+)*\b"
# pattern = r"(^|(?<=\s))([a-z0-9]+)\.*\-*\_*[a-z0-9]+@[a-z]+\-*[a-z]+\.[a-z]+\-*[a-z]+(\.[a-z]+\_*[a-z]+)*\b"
valid_emails = re.finditer(pattern, text_to_filter)
valid_emails = [vm.group() for vm in valid_emails]
print(*valid_emails, sep="\n")