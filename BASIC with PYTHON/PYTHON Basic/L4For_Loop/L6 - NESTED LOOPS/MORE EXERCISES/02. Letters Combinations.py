start_letter = input()
end_letter = input()
without_that_letter = input()
counter = 0

ord_start_letter = ord(start_letter)
ord_end_letter = ord(end_letter)
ord_without_that_letter = ord(without_that_letter)

for i in range(ord_start_letter, ord_end_letter + 1):
    for j in range(ord_start_letter, ord_end_letter + 1):
        for k in range(ord_start_letter, ord_end_letter + 1):
            if i != ord_without_that_letter and j != ord_without_that_letter and k != ord_without_that_letter:
                counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end= " ")

print(f"{counter}")

