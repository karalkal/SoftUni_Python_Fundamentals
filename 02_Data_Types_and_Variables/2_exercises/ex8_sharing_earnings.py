party_members = int(input())
days = int(input())
total = 0
for d in range(1, days + 1):
    if d % 10 == 0:
        party_members -= 2
    if d % 15 == 0:
        party_members += 5

    total += 50 - 2 * party_members

    if d % 3 == 0:
        total  -= 3 * party_members
    if d % 5 == 0:
        total  += 20 * party_members
        if d % 3 == 0:
            total -= 2 * party_members
bounty_p_p = int(total / party_members)
print(f"{party_members} companions received {bounty_p_p} coins each.")


