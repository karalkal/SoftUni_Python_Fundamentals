def check_password(string_to_test):
    check1, check2, check3 = False, False, False
    if len(string_to_test) < 6 or len(string_to_test) > 10:
        print("Password must be between 6 and 10 characters")
    else:
        check1 = True

    for i in range(len(string_to_test)):
        if ord(string_to_test[i]) < 48 or 89 < ord(string_to_test[i]) < 97 or ord(string_to_test[i]) > 122:
            print("Password must consist only of letters and digits")
            check2 = False
            break
        else:
            check2 = True

    count_nums = 0
    for j in range(len(string_to_test)):
        if 48 <= ord(string_to_test[j]) <= 57:
            count_nums += 1
    if count_nums < 2:
        print("Password must have at least 2 digits")
    else:
        check3 = True

    if check1 and check2 and check3:
        print("Password is valid")


user_input = input()
check_password(user_input)
