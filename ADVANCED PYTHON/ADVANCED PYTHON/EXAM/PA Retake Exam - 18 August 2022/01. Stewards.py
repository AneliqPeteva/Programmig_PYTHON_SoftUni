from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])

rotate = 0
seat_matches = []


while rotate != 10 and len(seat_matches) != 3:
    rotate += 1
    current_first_sequence = first_sequence.popleft()
    current_second_sequence = second_sequence.pop()
    first_seat = ""
    second_seat = ""

    ascii_symbol = chr(current_first_sequence + current_second_sequence)

    first_seat = f"{current_first_sequence}" + ascii_symbol
    second_seat = f"{current_second_sequence}" + ascii_symbol

    if first_seat in seats:
        seat_matches.append(first_seat)
        seats.remove(first_seat)
    elif second_seat in seats:
        seat_matches.append(second_seat)
        seats.remove(second_seat)
    else:
        first_sequence.append(current_first_sequence)
        second_sequence.appendleft(current_second_sequence)


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotate}")