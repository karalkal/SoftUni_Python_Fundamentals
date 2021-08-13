start = input()
finish = input()

def display_range_of_chars(a, b):
    for num in range(ord(a) + 1, ord(b)):
        print(chr(num), end=" ")


display_range_of_chars(start, finish)
