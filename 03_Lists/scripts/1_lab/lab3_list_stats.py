quantity = int(input())
neg = list()
pos = list()
for _ in range(1, quantity + 1):
    current_num = int(input())
    if current_num >= 0:
        pos.append(current_num)
    else:
        neg.append(current_num)
print(pos)
print(neg)
print(f"Count of positives: {len(pos)}. Sum of negatives: {sum(neg)}")
