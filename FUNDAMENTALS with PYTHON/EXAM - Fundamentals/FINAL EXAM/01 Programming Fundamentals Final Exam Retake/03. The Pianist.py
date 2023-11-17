number_of_pieces = int(input())
pieces_info = {}

for element in range(number_of_pieces):
    pieces = input().split("|")
    name = pieces[0]
    composer = pieces[1]
    key = pieces[2]

    pieces_info[name] = [composer, key]

while True:
    data_input = input().split("|")
    if data_input[0] == "Stop":
        break

    if data_input[0] == "Add":
        name = data_input[1]
        composer = data_input[2]
        key = data_input[3]
        if name in pieces_info.keys():
            print(f"{name} is already in the collection!")
        else:
            pieces_info[name] = [composer, key]
            print(f"{name} by {composer} in {key} added to the collection!")
    elif data_input[0] == "Remove":
        piece = data_input[1]
        if piece in pieces_info.keys():
            print(f"Successfully removed {piece}!")
            pieces_info.pop(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif data_input[0] == "ChangeKey":
        piece = data_input[1]
        new_key = data_input[2]
        if piece in pieces_info.keys():
            print(f"Changed the key of {piece} to {new_key}!")
            pieces_info[piece][1] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, values in pieces_info.items():
    print(f"{piece} -> Composer: {values[0]}, Key: {values[1]}")

