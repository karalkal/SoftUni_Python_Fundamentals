item_input = input()
dict_items_and_quantities = {}

while item_input != "stop":
    quantity_input = int(input())

    key = item_input
    value = quantity_input
    if key in dict_items_and_quantities:
        dict_items_and_quantities[key] += value
    else:
        dict_items_and_quantities[key] = value

    item_input = input()

for key, value in dict_items_and_quantities.items():
    print(key, "->", value)
