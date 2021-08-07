batches_of_water = int(input())
capacity = 255
total_filled = 0
for i in range(1, batches_of_water + 1):
    this_batch = int(input())
    if this_batch > capacity:
        print("Insufficient capacity!")
        continue
    capacity -= this_batch
    total_filled += this_batch
print(total_filled)
