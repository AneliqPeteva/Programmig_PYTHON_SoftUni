# Read user input
holidays = int(input())
work_day_gaming = (365 - holidays) * 63
# year = 365 day * 24 hour * 60 min = 525600
real_gaming = work_day_gaming + (holidays * 127)
result = abs(30000 - real_gaming)
hours = result // 60
minutes = result % 60

# Logic
if real_gaming < 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")