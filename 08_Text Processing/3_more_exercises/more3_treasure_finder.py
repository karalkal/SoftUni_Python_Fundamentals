the_key = input().replace(" ", "")
message = input()
reset_key = the_key
while message != "find":
    k = 0
    decoded = ""
    while len(the_key) < len(message):
        the_key += the_key[k]
        k += 1
        if k == len(reset_key):
            k = 0
    # print(the_key, len(the_key))
    # print(command, len(command))
    for i in range(len(message)):
        new_ch = ord(message[i]) - int(the_key[i])
        decoded += chr(new_ch)
    # print(decoded)
    item_found = decoded[decoded.find("&") + 1:decoded.rfind("&")]
    coordinates = decoded[decoded.find("<") + 1:decoded.find(">")]
    print(f"Found {item_found} at {coordinates}")
    the_key = reset_key

    message = input()

