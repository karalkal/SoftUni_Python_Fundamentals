def find_closest_to_zero(x1, y1, x2, y2):
    if x1 * x1 + y1 * y1 <= x2 * x2 + y2 * y2:
        result = f"({floor(x1)}, {floor(y1)})"
    else:
        result = f"({floor(x2)}, {floor(y2)})"
    return result

from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(find_closest_to_zero(x1, y1, x2, y2))
