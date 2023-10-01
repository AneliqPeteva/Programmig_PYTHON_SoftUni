sequence_of_targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command_type, index, other_info = [x for x in command.split()]
    index = int(index)
    other_info = int(other_info)
    if command_type == "Shoot":
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] -= other_info
            if sequence_of_targets[index] <= 0:
                del sequence_of_targets[index]
    elif command_type == "Add":
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets.insert(index, other_info)
        else:
            print("Invalid placement!")
    elif command_type == "Strike":
        start_radius = index - other_info
        end_radius = index + other_info + 1
        if 0 <= start_radius < end_radius < len(sequence_of_targets):
            del sequence_of_targets[start_radius:end_radius]
        else:
            print("Strike missed!")

    command = input()

print(*sequence_of_targets, sep="|")
