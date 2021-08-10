events_list = input().split("|")
num_of_events = len(events_list)
energy = 100
coins = 100
bankrupt = False

# while not bankrupt:
for i in range(num_of_events):
    # print(events_list[i])
    current_event = events_list[i].split("-")
    # print(current_event)

    type_of_event = current_event[0]
    value_of_event = int(current_event[1])
    # print(type_of_event, value_of_event, sep=" ")

    if type_of_event == "rest":
        if energy + value_of_event >= 100:
            value_of_event = 100 - energy  # we top up with energy until we reach 100
            energy = 100
        else:
            energy += value_of_event
        print(f"You gained {value_of_event} energy.")
        print(f"Current energy: {energy}.")

    elif type_of_event == "order":
        # energy -= 30   # !!!! CHECK THAT, unclear
        if energy - 30 >= 0:  # if fit enough
            energy -= 30
            coins += value_of_event
            print(f"You earned {value_of_event} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:  # any other input => have to spend coins
        if value_of_event < coins:  # have the money BUT IF EQUAL RETURNS ERROR
            coins -= value_of_event
            print(f"You bought {type_of_event}.")
        else:
            bankrupt = True
            break
if bankrupt:
    print(f"Closed! Cannot afford {type_of_event}.")
else:
    print("Day completed!", f"\nCoins: {coins}", f"\nEnergy: {energy}")
