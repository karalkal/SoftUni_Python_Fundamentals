class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment1 = Comment("ivan", "Yo", 4)
comment2 = Comment("pesho", "YoYo", 8)

print(comment1.username, comment2.username)
