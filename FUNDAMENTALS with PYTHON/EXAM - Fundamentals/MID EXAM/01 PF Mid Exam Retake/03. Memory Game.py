sequence_of_elements = input().split()
command = input()
number_of_moves = 0
while command != "end":
    first_index, second_index = [int(x) for x in command.split()]
    number_of_moves += 1
    len_elements = len(sequence_of_elements)

    if first_index == second_index or not 0 <= first_index < len_elements or not 0 <= second_index < len_elements:
        middle_sequence_of_element = int(len_elements / 2)
        element_insert = f'-{number_of_moves}a'
        sequence_of_elements = sequence_of_elements[:middle_sequence_of_element] + [element_insert, element_insert] + sequence_of_elements[middle_sequence_of_element:]
        print("Invalid input! Adding additional elements to the board")

    elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
        del sequence_of_elements[first_index]
        if first_index < second_index:
            second_index -= 1
        del sequence_of_elements[second_index]
    else:
        print("Try again!")

    if not sequence_of_elements:
        break

    command = input()

if sequence_of_elements:
    print("Sorry you lose :(\n", *sequence_of_elements)

else:
    print(f"You have won in {number_of_moves} turns!")




