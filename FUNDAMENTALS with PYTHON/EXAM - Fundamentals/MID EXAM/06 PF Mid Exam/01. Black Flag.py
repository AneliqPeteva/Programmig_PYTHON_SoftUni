
days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for current_day in range(1, days + 1):
    total_plunder += daily_plunder
    if current_day % 3 == 0:
        total_plunder += daily_plunder * 0.50
    if current_day % 5 == 0:
        total_plunder *= 0.70
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percent = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percent:.2f}% of the plunder.")



