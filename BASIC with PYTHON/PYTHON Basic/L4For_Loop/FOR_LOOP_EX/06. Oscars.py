# Read user input
name_actor = input()
point_academy = float(input())
n = int(input())
# Logic
for i in range(n):
    evaluator_name = input()
    point_from_evaluator = float(input())
    length_evaluator_name = len(evaluator_name)
    point_academy = point_academy + ((length_evaluator_name * point_from_evaluator) / 2)
    if point_academy >= 1250.5:
        break

# Print output
if point_academy >= 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {point_academy:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {(1250.5 - point_academy):.1f} more!")