def smallest_of_three_nums(a, b, c):
    if a < b and a < c:
        result = a
    elif b < a and b < c:
        result = b
    elif c < a and c < b:
        result = c
    return result


first = int(input())
second = int(input())
third = int(input())

print(smallest_of_three_nums(first, second, third))