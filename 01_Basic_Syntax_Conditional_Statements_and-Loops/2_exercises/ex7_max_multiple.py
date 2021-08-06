divisor = int(input())
bound = int(input())
while bound % divisor != 0:
    bound -= 1

print(bound)
