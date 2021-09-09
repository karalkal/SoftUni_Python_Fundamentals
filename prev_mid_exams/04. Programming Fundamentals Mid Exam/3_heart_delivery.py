houses = input().split("@")
houses = [int(x) for x in houses]
command = input()
visiting = 0
count = 0

has_done_the_job = False

while command != "Love!":
    visiting += int(command[4:])  # Problem was nums > 9

    if visiting > len(houses) - 1:
        visiting = 0

    if houses[visiting] == 0:
        print(f"Place {visiting} already had Valentine's day.")

    else:
        houses[visiting] -= 2

        if houses[visiting] == 0:
            print(f"Place {visiting} has Valentine's day.")
            count += 1

    command = input()

missed = len(houses) - count

if missed == 0:
    has_done_the_job = True

if has_done_the_job:
    print(f"Cupid's last position was {visiting}.\nMission was successful.")
else:
    print(f"Cupid's last position was {visiting}.\nCupid has failed {missed} places.")


