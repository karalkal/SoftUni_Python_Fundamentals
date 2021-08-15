def manipulate_value_depending_on_input(value, type):
    if type == "int":
        result = 2 * int(value)
    elif type == "real":
        result = f"{1.5 * float(value):.2f}"
    elif type == "string":
        result = "$" + value + "$"
    return result

type_of_input = input()
user_input = input()
print(manipulate_value_depending_on_input(user_input, type_of_input))