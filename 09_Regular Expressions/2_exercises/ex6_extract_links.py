import re

valid_links = []
pattern = r"www\.[A-Za-z0-9-]+\.[a-z]+(\.?[a-z-])*"
text_to_scan = input()
result = ""
while text_to_scan:
    result = re.finditer(pattern, text_to_scan)  # could contain more than 1 link, therefore not using search()
    # result contains 1 or more matches in this line
    for res in result:
        # print(res.group())
        valid_links.append(res.group())
        # once results appended to list, result literal is empty, expecting new input
        result = ""
    text_to_scan = input()
print("\n".join(valid_links))
