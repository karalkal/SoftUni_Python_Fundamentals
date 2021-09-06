energy = int(input())
distance = input()
count = 0
dead = False
while distance != "End of battle":
    distance = int(distance)
    if energy < distance:
        dead = True
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        break
    energy -= distance
    count += 1

    if count % 3 == 0:
        energy += count
    distance = input()
if not dead:
    print(f"Won battles: {count}. Energy left: {energy}" )


