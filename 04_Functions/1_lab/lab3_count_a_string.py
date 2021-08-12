def count_a_string(string, times):
    res = string * times
    return res


string = input()
times = int(input())

print(count_a_string(string, times))