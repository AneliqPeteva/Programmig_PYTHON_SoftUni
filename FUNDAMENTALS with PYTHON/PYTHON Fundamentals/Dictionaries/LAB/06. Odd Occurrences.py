words = input().split()
dict = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dict:
        dict[word_lower] = 0
    dict[word_lower] += 1

for (key, value) in dict.items():
    if value % 2 != 0:
        print(key, end=' ')