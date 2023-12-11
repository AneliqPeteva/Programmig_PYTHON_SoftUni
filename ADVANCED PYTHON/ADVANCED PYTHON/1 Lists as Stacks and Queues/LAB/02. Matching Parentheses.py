data = input()
indexes = []

for index in range(len(data)):
    ch = data[index]

    if ch == '(':
        indexes.append(index)
    elif ch == ')':
        l = indexes.pop()
        print(data[l:index + 1])