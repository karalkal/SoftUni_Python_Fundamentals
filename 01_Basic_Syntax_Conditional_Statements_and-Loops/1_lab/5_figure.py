user_num = int(input())
for rows_rising in range(1, user_num + 1):
    for stars in range(1, rows_rising + 1):
        print("*", end="")
    print()
for rows_decreasing in range(1, user_num + 1):
    for stars in range(rows_decreasing + 1, user_num + 1):
        print("*", end="")
    print()
