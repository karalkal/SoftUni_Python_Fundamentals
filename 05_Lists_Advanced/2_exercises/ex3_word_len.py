result = (x for x in input().split() if len(x) % 2 == 0)
print(*result, sep="\n")