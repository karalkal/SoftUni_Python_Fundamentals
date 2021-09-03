command = input()
total = 0
while command != "special" and command != "regular":
    component_price = float(command)
    if component_price <= 0:
        print("Invalid price!")
    else:
        total += component_price
    command = input()

if total == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {total * .2:.2f}$")
    print("-----------")

    if command == "special":
        total *= .9

    print(f"Total price: {total * 1.2:.2f}$")
