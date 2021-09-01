import re

string_to_filter = input()
pattern = r"^>>(?P<item>[A-Z][a-zA-Z]+)<<(?P<price>\d+((\.{1}\d+))?)\!(?P<quantity>\d+)$"
# pattern = r"^>>(?P<item>[a-zA-Z]+)<<(?P<price>[0-9]+(\.[0-9]+)*)\!(?P<quantity>\d+)"
# pattern = r"^>>(?P<item>[a-zA-Z]+)<<(?P<price>[0-9]+\.*[0-9]*)\!(?P<quantity>\d+)"
total = 0
items_bought = []
while string_to_filter != "Purchase":
    this_item_info = re.finditer(pattern, string_to_filter)
    for each_item in this_item_info:
        items_bought.append(each_item.group("item"))  # adds new items to list
        total += float(each_item.group("price")) * int(each_item.group("quantity"))
    string_to_filter = input()
print("Bought furniture:")
# print(*items_bought, sep="\n")  # IF ZERO items in list prints new line -> problem
for purchase in items_bought:
    print(purchase)
print(f"Total money spend: {total:.2f}")
