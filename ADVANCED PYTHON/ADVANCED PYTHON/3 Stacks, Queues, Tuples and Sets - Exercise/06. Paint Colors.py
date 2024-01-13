from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "green", "blue", "orange", "purple"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"}
}

result = []

while words:
    first_word = words.popleft()
    last_word = words.pop() if words else ""

    for color in (first_word + last_word, last_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for element in (first_word[:-1], last_word[:-1]):
            if element:
                words.insert(len(words) // 2, element)

for color in set(req_colors.keys()).intersection(result):
    if not req_colors[color].issubset(result):
        result.remove(color)

print(result)
