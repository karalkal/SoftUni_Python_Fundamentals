entries = int(input())
openig_br_count = 0
closing_br_count = 0
balanced = True
for i in range(1, entries + 1):
    character = input()
    if character == "(":
        openig_br_count += 1
    if character == ")":
        closing_br_count +=1

    if closing_br_count > openig_br_count:
        balanced = False
        break
    if openig_br_count > closing_br_count + 1:
        balanced = False
        break

if openig_br_count != closing_br_count:
    balanced = False

if not balanced:
    print("UNBALANCED")
else:
    print("BALANCED")


