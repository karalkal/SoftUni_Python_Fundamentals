import re
string_to_filter  = input()
pattern = r"\b_[a-zA-Z1-9]+\b"
results = re.findall(pattern, string_to_filter)
# for r in results:
#     print(r[1:], end=",")
results = [x[1:] for x in results]
print(*results, sep=",")