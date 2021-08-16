alive_men = input().split()
players = len(alive_men)
counter = int(input())
dead_men = []
survived = ""

while players > 0:

    # counting
    for i in range(counter - 1):  # index is 1 less
        survived = alive_men.pop(0)
        alive_men.append(survived)

    # i reaches counter
    dead = alive_men.pop(0)
    dead_men.append(dead)
    players -= 1

result = dead_men + alive_men  # initially thought last men are supposed to survive
print("[", end="")
print(*result, sep=",", end="")
print("]")
