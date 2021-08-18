class Party:
    def __init__(self):
        self.attendees = []


party1 = Party()  # instance of party

line = input()
while line != "End":
    party1.attendees.append(line)  # for each party append list
    line = input()

print(f"Going: {', '.join(party1.attendees)}")
print(f"Total: {len(party1.attendees)}")
