user_input = input()
dict_employees = {}
while user_input != "End":
    company, employee = user_input.split(" -> ")
    if company not in dict_employees:
        dict_employees[company] = [employee]
    elif company in dict_employees:
        if employee not in dict_employees[company]:  # THE real thing
            dict_employees[company] += [employee]
    user_input = input()

dict_employees = dict(sorted(dict_employees.items(), key=lambda x: x[0]))

for k, v in dict_employees.items():
    print(k)
    print("--", "\n-- ".join(v))
    # print("-- ", *v)
