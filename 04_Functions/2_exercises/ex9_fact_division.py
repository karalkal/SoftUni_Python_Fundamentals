def fact_division_of_two_nums(a, b):
    a_fact = 1
    b_fact = 1
    for i in range(a, 0, -1):
        a_fact *= i
    for j in range(b, 0, -1):
        b_fact *= j
    # print(a_fact)
    # print(b_fact)
    return f"{a_fact / b_fact:.2f}"


first = int(input())
second = int(input())
print(fact_division_of_two_nums(first, second))
