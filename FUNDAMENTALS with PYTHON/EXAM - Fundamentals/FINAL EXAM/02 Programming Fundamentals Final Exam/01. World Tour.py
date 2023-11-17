raw_string_stops = input()
command = input()

while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(raw_string_stops):
            raw_string_stops = raw_string_stops[:index] + string + raw_string_stops[index:]
        print(raw_string_stops)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(raw_string_stops) and 0 < end_index < len(raw_string_stops):
            raw_string_stops = raw_string_stops[:start_index] + raw_string_stops[end_index + 1:]
        print(raw_string_stops)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in raw_string_stops:
            raw_string_stops = raw_string_stops.replace(old_string, new_string)
        print(raw_string_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {raw_string_stops}")
