budget = float(input())
flour = float(input())
eggs = flour * .75
milk = flour * 1.25 / 4
price_koz = flour + eggs + milk
number_koz = 0
dyed_eggs = 0
while price_koz <= budget:  # we keep baking
    number_koz += 1
    budget -= price_koz
    dyed_eggs += 3
    if number_koz % 3 == 0:
        dyed_eggs = dyed_eggs - (number_koz - 2)
print(f"You made {number_koz} cozonacs! Now you have {dyed_eggs} eggs and {budget:.2f}BGN left.")