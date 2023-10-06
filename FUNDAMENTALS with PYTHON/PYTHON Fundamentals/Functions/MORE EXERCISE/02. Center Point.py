from math import floor, sqrt
def whats_closer(dist1, dist2):
    if dist1 <= dist2:
        return f"({x_1}, {y_1})"
    return f"({x_2}, {y_2})"


x_1 = floor(float(input()))
y_1 = floor(float(input()))
x_2 = floor(float(input()))
y_2 = floor(float(input()))

distance_point_1 = floor(sqrt(x_1 ** 2 + y_1 ** 2))
distance_point_2 = floor(sqrt(x_2 ** 2 + y_2 ** 2))
print(whats_closer(distance_point_1, distance_point_2))