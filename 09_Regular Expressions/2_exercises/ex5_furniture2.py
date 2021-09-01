import re

string_to_filter = input()
pattern = r"^>>(?P<item>[A-Za-z]+)<<(?P<price>\d+\.?\d*)?\!(?P<quantity>\d+)$"
# pattern = r"^>>(?P<item>[A-Z][a-zA-Z]+)<<(?P<price>\d+((\.{1}\d+))?)\!(?P<quantity>\d+)$"
# pattern = r"^>>(?P<item>[a-zA-Z]+)<<(?P<price>[0-9]+(\.[0-9]+)*)\!(?P<quantity>\d+)"
# pattern = r"^>>(?P<item>[a-zA-Z]+)<<(?P<price>[0-9]+\.*[0-9]*)\!(?P<quantity>\d+)"
total = 0
items_bought = []
while string_to_filter != "Purchase":
    this_item_info = re.match(pattern, string_to_filter)

    if this_item_info:
        items_bought.append(this_item_info.group("item"))  # adds new items to list
        total += float(this_item_info.group("price")) * int(this_item_info.group("quantity"))

    string_to_filter = input()
print("Bought furniture:")
# print(*items_bought, sep="\n")
for it in items_bought:
    print(it)
print(f"Total money spend: {total:.2f}")
