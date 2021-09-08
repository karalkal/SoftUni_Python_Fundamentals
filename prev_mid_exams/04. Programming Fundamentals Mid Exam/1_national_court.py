from math import floor

efficiency1 = int(input())
efficiency2 = int(input())
efficiency3 = int(input())
efficiency = efficiency1 + efficiency2 + efficiency3

customers = int(input())
count = 0

while customers > 0:
    count += 1
    customers = customers - efficiency
    if count % 4 == 0:
        customers = customers + efficiency

print(f"Time needed: {count}h.")
