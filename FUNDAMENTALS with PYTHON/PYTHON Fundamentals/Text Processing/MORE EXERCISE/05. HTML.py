title = input()
content = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")
comment = input()
while comment != "end of comments":
    print(f"<div>\n    {comment}\n</div>")
    comment = input()
