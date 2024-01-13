from collections import deque

def symbols_calculations(symbol, curr_bee, curr_nectar):
    if symbol == "+":
        return curr_bee + curr_nectar
    elif symbol == "-":
        return curr_bee - curr_nectar
    elif symbol == "*":
        return curr_bee * curr_nectar
    elif symbol == "/":
        return curr_bee / curr_nectar

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey_made = 0

while bees and nectar:
    current_bees, current_nectar = bees.popleft(), nectar.pop()

    if current_bees > current_nectar:
        bees.appendleft(current_bees)
    else:
        if current_nectar > 0:
            result = symbols_calculations(symbols.popleft(), current_bees,current_nectar)
            total_honey_made += abs(result)

print(f"Total honey made: {total_honey_made}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
#

# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = [int(x) for x in input().split()]
# symbols = deque(input().split())
#
# total_honey_made = 0
#
# while bees and nectar:
#     current_bees = bees.popleft()
#     current_nectar = nectar.pop()
#
#     if current_bees > current_nectar:
#         bees.appendleft(current_bees)
#     else:
#         if current_nectar > 0:
#             current_symbol = symbols.popleft()
#             if current_symbol == "+":
#                 total_honey_made += abs(current_bees + current_nectar)
#             elif current_symbol == "-":
#                 total_honey_made += abs(current_bees - current_nectar)
#             elif current_symbol == "*":
#                 total_honey_made += abs(current_bees * current_nectar)
#             elif current_symbol == "/":
#                 total_honey_made += abs(current_bees / current_nectar)
#
# print(f"Total honey made: {total_honey_made}")
# if bees:
#     print(f"Bees left: {', '.join(str(x) for x in bees)}")
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

