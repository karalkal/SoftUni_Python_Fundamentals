user_input = input()
stock = {}
while user_input != "statistics":
    pairs = user_input.split(": ")
    key, value = pairs[0], int(pairs[1])
    if key in stock.keys():
        stock[key] += value
    else:
        stock[key] = value

    user_input = input()
print("Products in stock:")

for key, value in stock.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
