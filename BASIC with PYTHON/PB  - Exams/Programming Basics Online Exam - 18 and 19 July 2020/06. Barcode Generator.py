start = input()
end = input()

start_first = int(start[0])
start_second = int(start[1])
start_third = int(start[2])
start_four = int(start[3])

end_first = int(end[0])
end_second = int(end[1])
end_third = int(end[2])
end_four = int(end[3])

for a in range(start_first, end_first + 1):
    for b in range(start_second, end_second + 1):
        for c in range(start_third, end_third + 1):
            for d in range(start_four, end_four + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end=" ")