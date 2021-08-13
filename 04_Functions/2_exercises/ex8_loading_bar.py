def progress_bar(num):
    first_digit = divisible_by_ten // 10
    if first_digit < 10:
        perc = first_digit * "%"
        dots = (10 - first_digit) * "."
        result = (f"{divisible_by_ten}% " + "[" + perc + dots + "]\n" + "Still loading...")
    else:
        result = "100% Complete!\n[%%%%%%%%%%]"

    return result


divisible_by_ten = int(input())
print(progress_bar(divisible_by_ten))
