stock_as_list = [x for x in input().split()]
searched_items = [x for x in input().split()]
dict_stock = {}

for i in range(0, len(stock_as_list), 2):
    dict_stock[stock_as_list[i]] = int(stock_as_list[i+1])

for s in range(len(searched_items)):
    if searched_items[s] not in dict_stock:
        print(f"Sorry, we don't have {searched_items[s]}")
    else:
        print(f"We have {dict_stock[searched_items[s]]} of {searched_items[s]} left")