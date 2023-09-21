from math import ceil
#User input
height_wall = int(input())
width_wall = int(input())
percent = int(input())
all_wall = height_wall * width_wall * 4
all_wall_for_coloring = ceil(all_wall - (all_wall * percent / 100))
#logic
while True:
    litres_color = input()
    if litres_color == "Tired!":
        print(f"{all_wall_for_coloring} quadratic m left.")
        break
    litres_color = int(litres_color)
    all_wall_for_coloring -= litres_color
    if all_wall_for_coloring == 0:
        print("All walls are painted! Great job, Pesho!")
        break
    if all_wall_for_coloring < 0:
        print(f"All walls are painted and you have {abs(all_wall_for_coloring)} l paint left!")
        break
#print output
