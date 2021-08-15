from math import floor, sqrt


def find_longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    line2 = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)

    if line1 >= line2:
        if x1 * x1 + y1 * y1 <= x2 * x2 + y2 * y2:
            result = f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        else:
            result = f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"

    else:
        if x3 * x3 + y3 * y3 <= x4 * x4 + y4 * y4:
            result = f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        else:
            result = f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"

    return result


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
print(find_longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
