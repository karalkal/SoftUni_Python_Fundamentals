user_input1 = input().split()
user_input2 = input().split()
user_input3 = input().split()

pos1 = user_input1[0]
pos2 = user_input1[1]
pos3 = user_input1[2]

pos4 = user_input2[0]
pos5 = user_input2[1]
pos6 = user_input2[2]

pos7 = user_input3[0]
pos8 = user_input3[1]
pos9 = user_input3[2]

if (pos1 == "1" and pos2 == "1" and pos3 == "1") \
        or (pos4 == "1" and pos5 == "1" and pos6 == "1") \
        or (pos7 == "1" and pos8 == "1" and pos9 == "1") \
        or (pos1 == "1" and pos5 == "1" and pos9 == "1") \
        or (pos3 == "1" and pos5 == "1" and pos7 == "1") \
        or (pos1 == "1" and pos4 == "1" and pos7 == "1") \
        or (pos2 == "1" and pos5 == "1" and pos8 == "1") \
        or (pos3 == "1" and pos6 == "1" and pos9 == "1"):
    print("First player won")


elif (pos1 == "2" and pos2 == "2" and pos3 == "2") \
        or (pos4 == "2" and pos5 == "2" and pos6 == "2") \
        or (pos7 == "2" and pos8 == "2" and pos9 == "2") \
        or (pos1 == "2" and pos5 == "2" and pos9 == "2") \
        or (pos3 == "2" and pos5 == "2" and pos7 == "2") \
        or (pos1 == "2" and pos4 == "2" and pos7 == "2") \
        or (pos2 == "2" and pos5 == "2" and pos8 == "2") \
        or (pos3 == "2" and pos6 == "2" and pos9 == "2"):
    print("Second player won")

else:
    print("Draw!")
