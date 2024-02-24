# def print_row(n, count):
#     print(' ' * (n - count), end="")
#     print(*['*'] * count)
#
#
# def print_triangle(n):
#     for count in range(1, n + 1):
#         print_row(n, count)
#
#
# def print_reversed_triangle(n):
#     for count in range(n - 1, 0, -1):
#         print_row(n, count)
#
#
# def print_rhombus(n):
#     print_triangle(n)
#     print_reversed_triangle(n)
#
#
# def print_square(n):
#     for _ in range(n):
#         print_row(n, n)
#
#
# n = int(input())
#
# print_rhombus(n)

def print_upper_rhombus(n):
    for row in range(1, n+1):
        print(" " * (n-row), "* "*row)

def print_botton_rhombus(n):
    for row in range(n - 1, 0, -1):
        print(" " * (n - row), "* " * row)

n = int(input())

print_upper_rhombus(n)
print_botton_rhombus(n)