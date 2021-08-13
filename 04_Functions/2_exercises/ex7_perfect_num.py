def check_if_perfect_number(num_to_check):
    st_list_of_div = []
    for div in range(1, num_to_check):  #excl num itself
        if num_to_check % div == 0:
            st_list_of_div.append(div)
    sum_of_divs = sum([int(d) for d in st_list_of_div])
    if sum_of_divs == num_to_check:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."
    

num_to_check = int(input())
print(check_if_perfect_number(num_to_check))



