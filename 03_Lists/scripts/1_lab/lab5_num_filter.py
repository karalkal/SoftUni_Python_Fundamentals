entries = int(input())
unfiltered_list = []
even = []
odd = []
neg = []
pos = []

for i in range(1, entries + 1):
    current_num = int(input())
    #    unfiltered_list.append(current_num)
    if current_num >= 0:
        pos.append(current_num)
    else:
        neg.append(current_num)
    if current_num % 2 == 0:
        even.append(current_num)
    else:
        odd.append(current_num)

filter_by = input()

if filter_by == "even":
    print(even)
elif filter_by == "odd":
    print(odd)
elif filter_by == "negative":
    print(neg)
if filter_by == "positive":
    print(pos)
