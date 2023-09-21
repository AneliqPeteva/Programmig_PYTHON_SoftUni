# Read user input
total_walking = 0

# Logic
while True:
    walking = input()
    if walking == "Going home":
        walking = int(input())
        total_walking += walking
        break
    walking = int(walking)
    total_walking += walking
    if total_walking >= 10000:
        break

diff = abs(total_walking - 10000)
if total_walking >= 10000:
    print(f"Goal reached! Good job!" )
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")



# Print output