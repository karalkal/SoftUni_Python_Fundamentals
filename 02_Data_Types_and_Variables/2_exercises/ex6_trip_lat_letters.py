num_of_letters = int(input())
for i in range(1, num_of_letters + 1):
    letter_first = chr(96+i)
    for j in range(1, num_of_letters + 1):
        letter_second = chr(96 + j)
        for k in range(1, num_of_letters + 1):
            letter_third= chr(96 + k)
            print(letter_first+letter_second+letter_third)
