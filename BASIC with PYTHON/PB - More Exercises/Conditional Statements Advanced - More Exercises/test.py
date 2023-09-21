# Read user input
# Logic
# Print output

# Read user input
x1 =float(input())
y1 =float(input())
x2 =float(input())
y2 =float(input())
x =float(input())
y =float(input())



if ((x == x1 or x == x2) and (y1 < y < y2)) or ((x1 < x < x2) and (y == y1 or y == y2)) or ((x == x1 or x == x2) and (y == y1 or y == y2)):
    print("Border")
else:
    print("Inside / Outside")
# Print output