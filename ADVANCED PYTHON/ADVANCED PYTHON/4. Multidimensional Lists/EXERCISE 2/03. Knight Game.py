# size = int(input())
# matrix = [list(input()) for _ in range(size)]
#
# positions = (
#     (-2, -1),  #нагоре 2 ляво 1
#     (-2, 1),   #нагоре 2 дясно 1
#     (-1, -2),  #нагоре 1 ляво 2
#     (-1, 2),   #нагоре 1 дясно 2
#     (2, 1),    #надолу 2 дясно 1
#     (2, -1),   #надолу 2 ляво 1
#     (1, 2),    #надолу 1 дясно 2
#     (1, -2),   #надолу 1 ляво 2
# )
#
# removed_knights = 0
#
# while True:
#     max_attacks = 0
#     knight_with_most_attacks_pos = []
#
#     for row in range(size):
#         for col in range(size):
#             if matrix[row][col] == "K":
#                 attacks = 0
#
#                 for position in positions:
#                     pos_row = row + position[0]
#                     pos_col = col + position[1]
#
#                     if 0 <= pos_row < size and 0 <= pos_col < size:
#                         if matrix[pos_row][pos_col] == "K":
#                             attacks += 1
#
#                 if attacks > max_attacks:
#                     knight_with_most_attacks_pos = [row, col]
#                     max_attacks = attacks
#
#     if knight_with_most_attacks_pos:
#         matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
#         removed_knights += 1
#     else:
#         break
#
# print(removed_knights)

size = int(input())
matrix = [list(input()) for _ in range(size)]

a= [-2,-1, 1, 2]
positions = [(x, y) for x in a for y in a if abs(x) != abs(y)]

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    pos_row = row + position[0]
                    pos_col = col + position[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)