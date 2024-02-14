rows, cols = [int(x) for x in input().split(", ")]

s_row, s_col, matrix, decorations, gifts, cookies, collected_all = 0, 0, [], 0, 0, 0, False

for row in range(rows):
    matrix.append(input().split())
    if "Y" in matrix[row]:
        s_row, s_col = row, matrix[row].index("Y")
        matrix[row][s_col] = "x"

command = input()
while command != "End" and not collected_all:
    direction, steps = [x if x.isalpha() else int(x) for x in command.split("-")]
    for step in range(steps):

        if direction == "up":
            s_row -= 1
        elif direction == "down":
            s_row += 1
        elif direction == "left":
            s_col -= 1
        elif direction == "right":
            s_col += 1

        if s_row == rows:
            s_row = 0
        elif s_row == -1:
            s_row = rows - 1

        elif s_col == cols:
            s_col = 0
        elif s_col == -1:
            s_col = cols - 1

        step_on = matrix[s_row][s_col]

        if step_on == "D":
            decorations += 1

        elif step_on == "G":
            gifts += 1

        elif step_on == "C":
            cookies += 1

        matrix[s_row][s_col] = "x"

        if any([x != "." and x != "x" for row_ in matrix for x in row_]):
            continue
        else:
            collected_all = True
            break

    if not collected_all:
        command = input()


matrix[s_row][s_col] = "Y"
if collected_all:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(*row) for row in matrix]