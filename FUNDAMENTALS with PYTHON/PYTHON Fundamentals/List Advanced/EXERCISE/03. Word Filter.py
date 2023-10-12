# words = input().split()
#
# for word in words:
#     if len(word) % 2 == 0:
#         print(word)

words = [word for word in input().split() if len(word) % 2 ==0]
print(*words, sep="\n")