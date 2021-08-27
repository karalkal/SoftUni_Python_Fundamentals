message = input().split()
for x in range(len(message)):
    if message[x] == ".-":
        message[x] = "A"
    elif message[x] == "-...":
        message[x] = "B"
    elif message[x] == "-.-.":
        message[x] = "C"
    elif message[x] == "-..":
        message[x] = "D"
    elif message[x] == ".":
        message[x] = "E"
    elif message[x] == "..-.":
        message[x] = "F"
    elif message[x] == "--.":
        message[x] = "G"
    elif message[x] == "....":
        message[x] = "H"
    elif message[x] == "..":
        message[x] = "I"
    elif message[x] == ".---":
        message[x] = "J"
    elif message[x] == "-.-":
        message[x] = "K"
    elif message[x] == ".-..":
        message[x] = "L"
    elif message[x] == "--":
        message[x] = "M"
    elif message[x] == "-.":
        message[x] = "N"
    elif message[x] == "---":
        message[x] = "O"
    elif message[x] == ".--.":
        message[x] = "P"
    elif message[x] == "--.-":
        message[x] = "Q"
    elif message[x] == ".-.":
        message[x] = "R"
    elif message[x] == "...":
        message[x] = "S"
    elif message[x] == "-":
        message[x] = "T"
    elif message[x] == "..-":
        message[x] = "U"
    elif message[x] == "...-":
        message[x] = "V"
    elif message[x] == ".--":
        message[x] = "W"
    elif message[x] == "-..-":
        message[x] = "X"
    elif message[x] == "-.--":
        message[x] = "Y"
    elif message[x] == "--..":
        message[x] = "Z"
    elif message[x] == "|":
        message[x] = " "

print(*message, sep="")
