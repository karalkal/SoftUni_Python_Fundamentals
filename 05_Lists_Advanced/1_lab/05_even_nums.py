list_of_nums = [int(x) for x in input().split(", ")]
'''index() only finds the first instance'''
# even_indexes = [list_of_nums.index(y) for y in list_of_nums if y % 2 == 0]
# print(even_indexes)

kur = [i for i in range(len(list_of_nums)) if list_of_nums[i] % 2 == 0]
print(kur)