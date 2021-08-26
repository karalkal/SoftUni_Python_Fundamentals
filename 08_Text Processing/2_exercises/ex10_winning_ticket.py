# def check_ticket(left, right):
#     win = "Kurec"
#
#     if "@@@@@@" in left and "@@@@@@" in right:
#         win = f"ticket{left + right} - 6@"
#     elif "######" in left and "######" in right:
#         win = f"ticket{left + right} - 6#"
#     elif "^^^^^^" in left and "^^^^^^" in right:
#         win = f"ticket{left + right} - 6^"
#     elif "$$$$$$" in left and "$$$$$$" in right:
#         win = f"ticket{left + right} - 6$"
#
#     return win


tickets = input().split(", ")
for tt in range(len(tickets)):
    this_ticket = tickets[tt].strip()
    if len(this_ticket) != 20:
        print("invalid ticket")
        continue

    left, right = this_ticket[:10], this_ticket[10:]
    # check_ticket(left, right)
    # 10
    if "@@@@@@@@@@" in left and "@@@@@@@@@@" in right:
        winning = f'ticket "{left + right}" - 10@ Jackpot!'
    elif "##########" in left and "##########" in right:
        winning = f'ticket "{left + right}" - 10# Jackpot!'
    elif "^^^^^^^^^^" in left and "^^^^^^^^^^" in right:
        winning = f'ticket "{left + right}" - 10^ Jackpot!'
    elif "$$$$$$$$$$" in left and "$$$$$$$$$$" in right:
        winning = f'ticket "{left + right}" - 10$ Jackpot!'
    # 9
    elif "@@@@@@@@@" in left and "@@@@@@@@@" in right:
        winning = f'ticket "{left + right}" - 9@'
    elif "#########" in left and "#########" in right:
        winning = f'ticket "{left + right}" - 9#'
    elif "^^^^^^^^^" in left and "^^^^^^^^^" in right:
        winning = f'ticket "{left + right}" - 9^'
    elif "$$$$$$$$$" in left and "$$$$$$$$$" in right:
        winning = f'ticket "{left + right}" - 9$'
    # 8
    elif "@@@@@@@@" in left and "@@@@@@@@" in right:
        winning = f'ticket "{left + right}" - 8@'
    elif "########" in left and "########" in right:
        winning = f'ticket "{left + right}" - 8#'
    elif "^^^^^^^^" in left and "^^^^^^^^" in right:
        winning = f'ticket "{left + right}" - 8^'
    elif "$$$$$$$$" in left and "$$$$$$$$" in right:
        winning = f'ticket "{left + right}" - 8$'
    # 7
    elif "@@@@@@@" in left and "@@@@@@@" in right:
        winning = f'ticket "{left + right}" - 7@'
    elif "#######" in left and "#######" in right:
        winning = f'ticket "{left + right}" - 7#'
    elif "^^^^^^^" in left and "^^^^^^^" in right:
        winning = f'ticket "{left + right}" - 7^'
    elif "$$$$$$$" in left and "$$$$$$$" in right:
        winning = f'ticket "{left + right}" - 7$'
    # 6
    elif "@@@@@@" in left and "@@@@@@" in right:
        winning = f'ticket "{left + right}" - 6@'
    elif "######" in left and "######" in right:
        winning = f'ticket "{left + right}" - 6#'
    elif "^^^^^^" in left and "^^^^^^" in right:
        winning = f'ticket "{left + right}" - 6^'
    elif "$$$$$$" in left and "$$$$$$" in right:
        winning = f'ticket "{left + right}" - 6$'

    else:
        winning = f'ticket "{left + right}" - no match'

    print(winning)
