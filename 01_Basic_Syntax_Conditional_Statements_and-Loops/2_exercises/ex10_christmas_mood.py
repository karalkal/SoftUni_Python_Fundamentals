quantity = int(input())
days = int(input())
mood = 0
cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        cost = cost + 2 * quantity
        mood += 5
    if day % 3 == 0:
        cost = cost + (5 + 3) * quantity
        mood += 13
    if day % 5 == 0:
        cost = cost + 15 * quantity
        mood += 17
        if day % 3 == 0:
            mood += 30
    if day % 10 == 0:
        mood -= 20
        cost = cost + 5 + 3 + 15
if days % 10 == 0:
    mood -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {mood}")
