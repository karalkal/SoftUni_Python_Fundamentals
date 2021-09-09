houses = input().split("@")
houses = [int(x) for x in houses]
command = input()
visiting = 0
count = 0

has_done_the_job = False

while command != "Love!":
    visiting += int(command[-1])

    if visiting > len(houses) - 1:
        visiting = visiting % (len(houses))

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
    print("Mission was successful.")
else:
    print(f"Cupid's last position was {visiting}.\nCupid has failed {missed} places.")


