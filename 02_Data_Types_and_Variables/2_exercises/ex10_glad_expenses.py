losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
for l in range(1, losses + 1):
    if l % 2 == 0:
        expenses += helmet_price
    if l % 3 == 0:
        expenses += sword_price
    if l % 6 == 0:
        expenses += shield_price
    if l % 12 == 0:
        expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

