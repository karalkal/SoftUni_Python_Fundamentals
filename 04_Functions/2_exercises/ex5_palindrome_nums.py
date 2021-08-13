def check_if_num_is_palindrome(num_to_check):
    times_to_check = len(num_to_check) // 2
    for i in range(times_to_check):
        b = (i * -1) - 1  # back index

        front_digit = int(num_to_check[i])
        back_digit = int(num_to_check[b])

        if front_digit != back_digit:
            return False  # if one pair is not equal, function returns False and stops

    return True # if hasn't returned False yet, num is palindrome


user_input = input().split(", ")

# check for each entry
for n in range(len(user_input)):
    current_num_as_str = user_input[n]

    # invoke function for each entry (it's still a string)
    result = check_if_num_is_palindrome(current_num_as_str)

    print(result)