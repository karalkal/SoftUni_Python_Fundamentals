num = int(input())
divided_times = 0
for i in range(1, num + 1):
    if num % i == 0:
        divided_times += 1
if divided_times > 2:
    print("False")
else:
    print("True")