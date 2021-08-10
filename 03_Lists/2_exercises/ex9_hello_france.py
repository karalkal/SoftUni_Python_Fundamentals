buying_list = input().split("|")
budget = float(input())
sales = 0
spent = 0
items_to_buy = []
going_to_France = False

for ci in range(len(buying_list)):
    current_item = buying_list[ci].split("->")
    # print(current_item)
    price_asked = float(current_item[1])
    if current_item[0] == "Clothes" and price_asked <= 50.00 \
            or current_item[0] == "Shoes" and price_asked <= 35.00 \
            or current_item[0] == "Accessories" and price_asked <= 20.50:
        items_to_buy.append(buying_list[ci])

for bought in range(len(items_to_buy)):
    if going_to_France:
        break
    current_item = items_to_buy[bought].split("->")
    price_asked = float(current_item[1])

    if price_asked <= budget:  # buy, buy, buy but i price too high don't break
        spent += price_asked
        budget -= price_asked
        sales += price_asked * 1.4
        print(f"{price_asked * 1.4:.2f}", end=" ")
        if sales + budget >= 150:
            going_to_France = True
            break
print()
print(f"Profit: {sales - spent:.2f}")

if going_to_France:
    print("Hello, France!")
else:
    print("Time to go.")
