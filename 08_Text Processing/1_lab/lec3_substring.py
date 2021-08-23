remove_this = input()
original_str = input()
while remove_this in original_str:
    original_str = original_str.replace(remove_this, "")
print(original_str)
