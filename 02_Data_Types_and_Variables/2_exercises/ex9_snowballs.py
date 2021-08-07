iterations = int(input())
best_result = 0
winning_snow = 0
winning_time = 0
winning_quality = 0
for ball in range(1, iterations + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    formula = (snowball_snow / snowball_time) ** snowball_quality
    if formula > best_result:
        best_result = formula
        winning_snow = snowball_snow
        winning_time = snowball_time
        winning_quality = snowball_quality
print(f"{winning_snow} : {winning_time} = {best_result:.0f} ({winning_quality})")
