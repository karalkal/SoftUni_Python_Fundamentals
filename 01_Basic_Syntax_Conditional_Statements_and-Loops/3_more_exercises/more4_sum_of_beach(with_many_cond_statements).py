string = input()
counter = 0

for el in range(len(string)):
    if string[el] == "s" or string[el] == "S":
        if string[el + 1] == "a" and el + 3 <= len(string) - 1 or string[el + 1] == "A" and el + 3 <= len(string) - 1:
            if string[el + 2] == "n" or string[el + 2] == "N":
                if string[el + 3] == "d" or string[el + 3] == "D":
                    counter += 1
        elif string[el + 1] == "u" and el + 2 <= len(string) - 1 or string[el + 1] == "U" and el + 2 <= len(string) - 1:
            if string[el + 2] == "n" or string[el + 2] == "N":
                counter += 1
    elif string[el] == "w" and el + 4 <= len(string) - 1 or string[el] == "W" and el + 4 <= len(string) - 1:
        if string[el + 1] == "a" or string[el + 1] == "A":
            if string[el + 2] == "t" or string[el + 2] == "T":
                if string[el + 3] == "e" or string[el + 3] == "E":
                    if string[el + 4] == "r" or string[el + 4] == "R":
                        counter += 1
    elif string[el] == "f" and el + 3 <= len(string) - 1 or string[el] == "F" and el + 3 <= len(string) - 1:
        if string[el + 1] == "i" or string[el + 1] == "I":
            if string[el + 2] == "s" or string[el + 2] == "S":
                if string[el + 3] == "h" or string[el + 3] == "H":
                    counter += 1

print(counter)