sequence_of_elements = input().split()
command = input()
counter_moves = 0

while command != 'end':
    command = command.split()
    first_index = int(command[0])
    second_index = int(command[1])
    counter_moves += 1
    len_sequence_of_elements = len(sequence_of_elements)
    middle_sequence_of_elements = int(len_sequence_of_elements / 2)
    if not 0 <= first_index < len_sequence_of_elements or not 0 <= second_index < len_sequence_of_elements or first_index == second_index:
        print("Invalid input! Adding additional elements to the board")
        sequence_of_elements.insert(middle_sequence_of_elements, f"-{counter_moves}a")
        sequence_of_elements.insert(middle_sequence_of_elements, f"-{counter_moves}a")
    elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
        if second_index > first_index:
            sequence_of_elements.pop(second_index)
            sequence_of_elements.pop(first_index)
        else:
            sequence_of_elements.pop(first_index)
            sequence_of_elements.pop(second_index)
    elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {counter_moves} turns!")
        break
    command = input()

if len(sequence_of_elements) > 0:
    print("Sorry you lose :(")
    print(*sequence_of_elements)

