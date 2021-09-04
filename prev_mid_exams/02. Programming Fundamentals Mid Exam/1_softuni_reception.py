productivity_per_hour = int(input()) + int(input()) + int(input())
total = int(input())
time = 0

while total > 0:
    total = total - productivity_per_hour
    time += 1
    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")
