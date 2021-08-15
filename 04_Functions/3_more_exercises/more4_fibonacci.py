def tribonacci_seq(how_many):
    num1 = 0
    num2 = 1
    num3 = 1
    if how_many == 1:
        result = "1"
        return result

    result = ""
    # print(num2, end=" ")
    # print(num3, end=" ")

    result = str(num2) + " " + str(num3)
    for i in range(how_many - 2):
        num4 = num1 + num2 + num3
        # print(num4, end=" ")
        num1, num2, num3 = num2, num3, num4
        result += " " + str(num4)

    return result


num = int(input())
print(tribonacci_seq(num))
