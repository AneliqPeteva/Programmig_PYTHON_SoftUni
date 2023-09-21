m = int(input())
counter = 0

#logic
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == m and a < b and c > d:
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        true_password = f"{a}{b}{c}{d}"




if counter >= 4:
    print(f"\nPassword: {true_password}")
else:
    print(f"\nNo!")