herd = input()
if herd[len(herd) - 1] == "f":
    print("Please go away and stop eating my sheep")
else:
    for animal in range(len(herd) - 1, 0, -1):
        if herd[animal] == "f":  # we have spotted the wolf and need to get to the sheep
            #  ", sheep" is exactly 7 chars. From "f" we go back  
            doomed_sheep = str(round((len(herd) - animal - 1) / 7))
            print("Oi! Sheep number " + doomed_sheep + "! You are about to be eaten by a wolf!")
