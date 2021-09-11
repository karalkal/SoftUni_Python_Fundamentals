duration_days = int(input())
daily_plunder = int(input())
to_reach = float(input())
winnings = 0

for d in range(1, duration_days + 1):
    winnings += daily_plunder
    if d % 3 == 0:
        winnings += .5 * daily_plunder
    if d % 5 == 0:
        winnings = winnings * .7
if winnings >= to_reach:
    print(f"Ahoy! {winnings:.2f} plunder gained.")
else:
    percentage = winnings * 100 / to_reach
    print(f"Collected only {percentage:.2f}% of the plunder.")