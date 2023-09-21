x_high_wall = float(input())
y_length_side_wall = float(input())
h_high_roof = float(input())

# wall
side_walls = ((x_high_wall * y_length_side_wall) * 2) - ((1.5 * 1.5) * 2)
front_back_wall = (x_high_wall * x_high_wall) * 2 - (1.2 * 2)

# roof
roof_sides = (x_high_wall * y_length_side_wall) * 2
roof_triangles = 2 * (x_high_wall * h_high_roof / 2)

# total
total_green = front_back_wall + side_walls
total_red = roof_sides + roof_triangles

final_sum_green = total_green / 3.4
final_sum_red = total_red / 4.3

print(float(f'{final_sum_green:.2f}'))
print(float(f'{final_sum_red:.2f}'))