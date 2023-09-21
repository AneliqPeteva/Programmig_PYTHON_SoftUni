# Read user input
n = int(input())
odd_sum = 0
odd_min = 0
odd_max = 0
even_sum = 0
even_min = 0
even_max = 0

# Logic
for i in range(1, n+1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        if i == 2:
            even_min = num
            even_max = num
        if even_min > num:
            even_min = num
        if even_max < num:
            even_max = num
    else:
        odd_sum += num
        if i == 1:
            odd_min = num
            odd_max = num
        if odd_min > num:
            odd_min = num
        if odd_max < num:
            odd_max = num

if n == 0:
    print(f"OddSum=0.00,")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum=0.00,")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
elif even_min == 0 and even_max == 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
elif odd_min == 0 and odd_max == 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")