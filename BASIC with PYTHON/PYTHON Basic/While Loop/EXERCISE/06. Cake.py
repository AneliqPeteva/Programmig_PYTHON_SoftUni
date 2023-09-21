
# Read user input
length_cake = int(input())
width_cake = int(input())
user_input = input()

# Logic
count_piece_cake = length_cake * width_cake
while True:
    if user_input == "STOP":
        print(f"{count_piece_cake} pieces are left." )
        break
    user_input = int(user_input)
    count_piece_cake -= user_input
    if count_piece_cake < 0:
        print(f"No more cake left! You need {abs(count_piece_cake)} pieces more.")
        break
    user_input = input()


# Print output
