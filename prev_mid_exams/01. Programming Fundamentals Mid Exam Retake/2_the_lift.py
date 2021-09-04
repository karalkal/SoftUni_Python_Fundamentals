num = int(input())
lift = [int(x) for x in input().split() if 0 <= int(x) <= 4]
remaining_seats = False

for i in range(0, len(lift)):
    if lift[i] < 4 and num >= 0:
        available_seats = 4 - lift[i]
        num -= available_seats

        if num < 0:
            lift[i] = 4 + num
            remaining_seats = True
            break
        else:
            lift[i] = 4
            if num == 0:
                break

if num > 0:
    print(f"There isn't enough space! {num} people in a queue!")
if remaining_seats:
    print("The lift has empty spots!")

print(*lift, sep=" ")
