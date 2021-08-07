num = int(input())
stringed_num = str(num)
for i in range(1, num + 1):
    sum_of_digits = i // 10 + i % 10
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")


