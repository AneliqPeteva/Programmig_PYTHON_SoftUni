x = float(input())
y = float(input())
h = float(input())

green_paint_consumption = 3.4
red_paint_consumption = 4.3

front_back_walls = 2 * (x * x)
door = 1.2 * 2
sidewall = 2 * (x * y)
window = 1.5 * 1.5
total_area_wall = front_back_walls + sidewall - door - 2 * window
green_paint = total_area_wall / green_paint_consumption

total_area_roof = 2 * (x * y) + (2 * (x * h/2))
red_paint = total_area_roof / red_paint_consumption

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")