def check_if_product_is_pos(n1, n2, n3):
    if (num1 < 0 and num2 > 0 and num3 > 0) \
            or (num2 < 0 and num1 > 0 and num3 > 0) \
            or (num3 < 0 and num1 > 0 and num2 > 0) \
            or (num1 < 0 and num2 < 0 and num3 < 0):  # all three are neg
        return "negative"
    elif num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    else:
        return "positive"


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(check_if_product_is_pos(num1, num2, num3))
