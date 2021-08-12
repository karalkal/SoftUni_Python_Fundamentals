def calculator(a, b, action):
    if action == 'multiply':
        res = int(a * b)
    elif action == 'divide':
        res = int(a / b)
    elif action == 'add':
        res = int(a + b)
    elif action == 'subtract':
        res = int(a - b)
    return res


action = input()
a = int(input())
b = int(input())
print(calculator(a, b, action))
