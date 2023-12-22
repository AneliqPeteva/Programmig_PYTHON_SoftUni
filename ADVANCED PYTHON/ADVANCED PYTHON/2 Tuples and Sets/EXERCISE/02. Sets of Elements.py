n, m = [int(x) for x in input().split()]
first_set = set(int(input()) for _ in range(n))
second_set = set(int(input()) for _ in range(m))
unique_element = first_set.intersection(second_set)
# intersection - показва елементите, който ги има и в двата сета
print(*unique_element, sep="\n")
