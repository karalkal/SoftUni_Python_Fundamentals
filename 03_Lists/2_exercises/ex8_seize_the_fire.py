fires = input().split("#")
initial_len = len(fires)
water = int(input())
effort = 0
total_fire = 0
valid_fires = []

# filter fires list for values
for f in range(initial_len):
    current_fire = fires[f].split(" = ")
    range_of_fire = int(current_fire[1])
    if current_fire[0] == "Low" and 1 <= range_of_fire<= 50  or\
            current_fire[0] == "Medium" and  51 <= range_of_fire <= 80 or \
            current_fire[0] == "High" and  81 <= range_of_fire <= 125:
        valid_fires.append(current_fire)

# print(fires)  # now the real action starts
print("Cells:")
for r in range(len(valid_fires)):
    current_fire = valid_fires[r]
    range_of_fire = int(current_fire[1])

    if water >= range_of_fire:
        print(f" - {range_of_fire}")
        water -= range_of_fire
        total_fire += range_of_fire
        effort += range_of_fire * .25
    else:
        continue
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
