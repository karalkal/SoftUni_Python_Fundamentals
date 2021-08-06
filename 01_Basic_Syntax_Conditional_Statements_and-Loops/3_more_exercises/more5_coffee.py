command = input()
coffee_count = 0
i_am_asleep = False
while command != "END":
    if command == "coding":
        coffee_count += 1
    elif command == "CODING":
        coffee_count += 2
    elif command == "dog" or command == "cat":
        coffee_count += 1
    elif command == "DOG" or command == "CAT":
        coffee_count += 2
    elif command == "movie":
        coffee_count += 1
    elif command == "MOVIE":
        coffee_count += 2
    if coffee_count > 5:
        print("You need extra sleep")
        i_am_asleep = True
        break

    command = input()
if not i_am_asleep:
    print(coffee_count)
