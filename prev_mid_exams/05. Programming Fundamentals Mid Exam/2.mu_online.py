initial_list = input().split("|")
health = 100
coins = 0
am_alive = True
room_no = 0

for i in range(len(initial_list)):
    room_no += 1
    current_action = initial_list[i].split()
    action = current_action[0]
    value = int(current_action[1])
    # print(action, value)

    if action == "potion":
        if health + value >= 100:  # if it happens to exceed 100
            value = 100 - health
            health = 100
        else:
            health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        coins += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value
        if health <= 0:
            am_alive = False
            print(f"You died! Killed by {action}.")
            # room_no -= 1  # SUPPOSED TO BE BUT ISN'T - one less as we don't pass the room
            print(f"Best room: {room_no}")
            break
        else:
            print(f"You slayed {action}.")

if am_alive:
    print(f"You've made it!\nBitcoins: {coins}\nHealth: {health}")