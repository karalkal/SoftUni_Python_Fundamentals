user_input = input()

def sum_evens_and_odds(num_as_str):
    evens, odds = [], []
    for i in range(len(num_as_str)):
        if int(num_as_str[i]) % 2 == 0:
            evens.append(int(num_as_str[i]))
        else:
            odds.append(int(num_as_str[i]))

    print(f"Odd sum = {sum(odds)}, Even sum = {sum(evens)}")


sum_evens_and_odds(user_input)
