quantity = int(input())
atoms_list = []
position = 0
while quantity > 0:
    position += 1
    max_value = 2 * position ** 2

    if max_value >= quantity:
        atoms_list.append(quantity)
        break

    quantity -= max_value
    atoms_list.append(max_value)
print(atoms_list)

