text_to_process = input()
digits = ""
letters = ""
others = ""
for sym in text_to_process:
    if sym.isdigit():
        digits += sym
    elif sym.isalpha():
        letters += sym
    else:
        others += sym

print(f"{digits}\n{letters}\n{others}")
