ROWS = 6
COLS = 7
WINNER_LENGTH = 4

directions_mapper = [
    (1, 0),     # down
    (0, -1),    # left
    (-1, -1),   # up left
    (-1, 1),    # up right
]


class FullColumnError(Exception):
    pass


def print_matrix(matrix):
    [print(row) for row in matrix]


def is_valid_number(selected_column_index):
    return 0 <= selected_column_index < COLS


def pos_player_number(col_index, matrix, player_):
    for row_index in range(ROWS-1, -1, -1):
        if matrix[row_index][col_index] == 0:
            matrix[row_index][col_index] = player_
            return row_index, col_index
    else:
        raise FullColumnError


def is_valid_place(row_index_to_check, col_index_to_check):
    return 0 <= row_index_to_check < ROWS and 0 <= col_index_to_check < COLS


def stated_directions_count(row, col, row_movement, col_movement, matrix, player_):
    count = 0
    for index in range(1, WINNER_LENGTH):
        row_index_to_check = row + row_movement * index
        col_index_to_check = col + col_movement * index
        if not is_valid_place(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player_:
            break
        count += 1
    return count


def opposite_direction_count(row, col, row_movement, col_movement, matrix, player_):
    count = 0
    for index in range(1, WINNER_LENGTH):
        row_index_to_check = row - row_movement * index
        col_index_to_check = col - col_movement * index
        if not is_valid_place(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player_:
            break
        count += 1
    return count


def is_winner(row, col, matrix, player_):
    for row_movement, col_movement in directions_mapper:
        count_direction = stated_directions_count(row, col, row_movement, col_movement, matrix, player_)
        count_opposite_direction = opposite_direction_count(row, col, row_movement, col_movement, matrix, player_)
        if (count_direction + count_opposite_direction) >= (WINNER_LENGTH - 1):
            return True
    return False


matrix_game = [[0] * COLS for _ in range(ROWS)]
print_matrix(matrix_game)

player = 1

while True:
    try:
        selected_col_number = int(input(f"Player {player}, please choose a column: "))
        selected_col_index = selected_col_number - 1
        if not is_valid_number(selected_col_index):
            raise ValueError
        current_row, current_col = pos_player_number(selected_col_index, matrix_game, player)
        if is_winner(current_row, current_col, matrix_game, player):
            print_matrix(matrix_game)
            print(f"Game over!!! The Winner is Player {player}!")
            break
        print_matrix(matrix_game)
    except ValueError:
        print(f"Incorrect number! Player {player}, please choose number between 1 and {COLS}")
        continue
    except FullColumnError:
        print(f"Player {player}, this column is full! Please choose another one!")
        continue

    player += 1
    player = 2 if player % 2 == 0 else 1