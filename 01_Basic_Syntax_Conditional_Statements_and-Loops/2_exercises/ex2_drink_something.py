age = int(input())
if age <= 14:
    to_drink = "toddy"
elif age <= 18:
    to_drink = "coke"
elif age <= 21:
    to_drink = "beer"
else:
    to_drink = "whisky"
print(f"drink {to_drink}")
