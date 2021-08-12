def prices_calc(item, quantity):
    total = 0
    if item == "coffee":
        total = quantity * 1.50
    elif item == "water":
        total = quantity * 1
    elif item == "coke":
        total = quantity * 1.40
    elif item == "snacks":
        total = quantity * 2
    return f"{total:.2f}"


item = input()
quantity = int(input())

print(prices_calc(item, quantity))
