title = "<h1>\n" + "    " + input() + "\n</h1>"
article = "<article>\n" + "    " + input() + "\n</article>"
comment = input()
print(title)
print(article)
while comment != "end of comments":
    div = "<div>\n" + "    " + comment + "\n</div>"
    print(div)

    comment = input()