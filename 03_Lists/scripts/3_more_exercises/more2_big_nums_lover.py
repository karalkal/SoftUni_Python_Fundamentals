initial_list = input().split()

# sort() changes the list directly and doesn't return any value,
# while sorted() doesn't change the list and returns the sorted list

initial_list.sort(reverse=True)
new_list = [int(x) for x in initial_list]
print(*new_list, sep="")
