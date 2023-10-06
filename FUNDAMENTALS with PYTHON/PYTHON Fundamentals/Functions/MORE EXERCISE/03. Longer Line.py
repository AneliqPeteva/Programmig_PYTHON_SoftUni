from math import floor, sqrt
def whats_closer(arg1, arg2, arg3, arg4):
    one = arg1 + arg2
    two = arg3 + arg4
    if one > two:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"
    elif one < two:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"
    else:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"


x1, x2, y1, y2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(
    float(input()))
z1, z2, v1, v2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(
    float(input()))

sum_x = floor(abs(x1) + abs(x2))
sum_y = floor(abs(y1) + abs(y2))
sum_z = floor(abs(z1) + abs(z2))
sum_v = floor(abs(v1) + abs(v2))
print(whats_closer(sum_x, sum_y, sum_z, sum_v))