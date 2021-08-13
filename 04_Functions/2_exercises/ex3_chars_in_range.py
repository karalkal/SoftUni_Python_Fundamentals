start = input()
finish = input()

def display_range_of_chars(a, b):
    first_ascii  = ord(a)
    second_ascii  = ord(b)
    ascii_list = []
    for num in range(first_ascii + 1, second_ascii):
        ascii_list.append(num)
    letter_list = [chr(x) for x in ascii_list]
    return letter_list

print(*display_range_of_chars(start, finish))
