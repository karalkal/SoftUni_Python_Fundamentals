num_of_entries = int(input())
parking_database = {}
for i in range(num_of_entries):
    entry = [x for x in input().split()]

    if entry[0] == "register":
        action, name, reg_no = entry
        if name not in parking_database.keys():
            parking_database[name] = reg_no
            print(f"{name} registered {reg_no} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_database[name]}")

    if entry[0] == "unregister":
        action, name = entry
        if name in parking_database.keys():
            parking_database.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for k, v in parking_database.items():
    print(k + " => " + v)
