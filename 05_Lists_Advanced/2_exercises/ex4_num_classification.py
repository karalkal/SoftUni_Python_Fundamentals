nums = [int(x) for x in input().split(", ")]
pos = [x for x in nums if x >= 0]
neg = [x for x in nums if x < 0]
even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]
print("Positive:", end=" ")
print(*pos, sep=", ")
print("Negative:", end=" ")
print(*neg, sep=", ")
print("Even:", end=" ")
print(*even, sep=", ")
print("Odd:", end=" ")
print(*odd, sep=", ")