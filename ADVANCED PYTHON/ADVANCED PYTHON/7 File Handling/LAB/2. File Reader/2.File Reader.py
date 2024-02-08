import os


WORKING_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIR_PATH, "numbers.txt")

with open("numbers.txt", "r") as file:
    total_sum = 0
    for line in file:
        number = int(line)
        total_sum += number

print(total_sum)