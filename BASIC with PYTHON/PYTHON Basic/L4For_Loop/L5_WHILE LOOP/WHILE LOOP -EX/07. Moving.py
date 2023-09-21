# Read user input
length_of_free_space = int(input())
width_of_free_space = int(input())
height_of_free_space = int(input())
number_of_boxes = input()
all_number_of_boxes = 0
# Logic
total_free_space = length_of_free_space * width_of_free_space * height_of_free_space
while True:
    if number_of_boxes == "Done":
        print(f"{abs(total_free_space)} Cubic meters left.")
        break
    number_of_boxes = int(number_of_boxes)
    total_free_space -= number_of_boxes

    if total_free_space < 0:
        print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")
        break
    number_of_boxes = input()
# Print output