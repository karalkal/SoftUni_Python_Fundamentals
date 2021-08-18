class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_as_objects = []
command = input()
while command != "Stop":
    command = command.split()
    sender, receiver, content = command[0], command[1], command[2]
    email_instance = Email(sender, receiver, content)
    emails_as_objects.append(email_instance)
    command = input()

to_send = [(int(x)) for x in input().split(", ")]
for s in to_send:
    emails_as_objects[s].send()  # each email with valid index send to function to change status

for email_instance in emails_as_objects:
    print(email_instance.get_info())

