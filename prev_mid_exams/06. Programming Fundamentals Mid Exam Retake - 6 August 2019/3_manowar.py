pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
# print(pirate_ship)
# print(war_ship)
max_health = int(input())
command = input()
won = False
lost = False

while command != "Retire":
    command = command.split()

    if command[0] == "Fire":
        index_to_attack, damage = int(command[1]), int(command[2])
        if 0 <= index_to_attack < len(war_ship):
            war_ship[index_to_attack] -= damage
            if war_ship[index_to_attack] <= 0:
                won = True
                break

    elif command[0] == "Defend":
        from_index, to_index, damage = int(command[1]), int(command[2]), int(command[3])
        if 0 <= from_index <= to_index < len(pirate_ship):  # if index is valid
            for d in range(from_index, to_index + 1):
                pirate_ship[d] -= damage

            for i in range(len(pirate_ship)):
                if pirate_ship[i] <= 0:
                    lost = True
                    break
    elif command[0] == "Repair":
        index_to_repair, health = int(command[1]), int(command[2])
        if 0 <= index_to_repair < len(pirate_ship):
            pirate_ship[index_to_repair] += health
            if pirate_ship[index_to_repair] > max_health:
                pirate_ship[index_to_repair] = max_health

    elif command[0] == "Status":
        damaged = [x for x in pirate_ship if x < max_health * .2]
        print(f"{len(damaged)} sections need repair.")

    command = input()

if lost:
    print("You lost! The pirate ship has sunken.")
elif won:
    print("You won! The enemy ship has sunken.")
else:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
