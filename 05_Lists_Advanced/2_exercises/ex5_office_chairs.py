count = 0
game_on = True
for r in range(int(input())):
    entry = input().split()
    if len(entry[0]) < int(entry[1]):  # not enough chairs
        print(f"{int(entry[1]) - len(entry[0])} more chairs needed in room {r+1}")
        game_on = False
    else:
        count += len(entry[0]) - int(entry[1])
if game_on:
    print(f"Game On, {count} free chairs left")

