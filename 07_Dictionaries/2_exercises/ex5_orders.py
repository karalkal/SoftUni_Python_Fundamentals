new_order = input()
dict_inventory = {}
while new_order != "buy":
    new_order = new_order.split()
    item, price, quantity = new_order[0], float(new_order[1]), int(new_order[2])

    if item not in dict_inventory.keys():
        dict_inventory[item] = [price, quantity]
    else:
        old_quantity = dict_inventory[item][1]
        dict_inventory[item] = [price, old_quantity + quantity]

    # print(dict_inventory)
    new_order = input()
for k, v in dict_inventory.items():
    print(k + " -> " + f"{v[0] * v[1]:.2f}")