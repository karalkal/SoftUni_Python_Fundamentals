old_happiness = [int(x) for x in input().split()]
factor = int(input())
new_happiness = []  #[y for y + factor in old_happiness]
for y in old_happiness:
    y = y + factor
    new_happiness.append(y)
avg_happiness = (sum(new_happiness) / len(new_happiness))
happy_list = [x for x in new_happiness if x >= avg_happiness]
if len(happy_list) * 2 >= len(new_happiness):
    print(f"Score: {len(happy_list)}/{len(new_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_list)}/{len(new_happiness)}. Employees are not happy!")
