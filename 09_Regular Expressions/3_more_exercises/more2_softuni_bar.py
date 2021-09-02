import re

pattern = r"%([A-Z][a-z]+)%.*<(\w+)>.*\|([0-9]+)\|[^0-9]*((?P<whole>[0-9]+)\.?(?P<decimal>[0-9]?)(?P<units>[0-9]?))\$"
total = 0
while True:
    purchase = input()
    if purchase == "end of shift":
        break
    else:
        matched_purchase = re.finditer(pattern, purchase)
        for match in matched_purchase:
            who, what, quantity, price = match.group(1), match.group(2), int(match.group(3)), int(match.group("whole"))
            if match.group("decimal"):
                price += int(match.group("decimal")) / 10
            if match.group("units"):
                price += int(match.group("units")) / 100
            total += price * quantity

            print(f"{who}: {what} - {quantity * price:.2f}")
print(f"Total income: {total:.2f}")
