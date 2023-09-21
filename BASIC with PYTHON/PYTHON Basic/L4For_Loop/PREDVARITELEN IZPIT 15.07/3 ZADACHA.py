count_dancers = int(input())
count_point = float(input())
season = input()
place = input()
prize = 0


if place == "Bulgaria":
    prize = count_point * count_dancers
    if season == "summer":
        prize *= 0.95
    elif season == "winter":
        prize *= 0.92
elif place == "Abroad":
    prize = count_point * count_dancers + (count_point * count_dancers * 0.5)
    if season == "summer":
        prize *= 0.90
    elif season == "winter":
        prize *= 0.85

left_prize = prize - (prize * 0.75)
prize_for_one_people = left_prize / count_dancers

print(f"Charity - {prize * 0.75:.2f}")
print(f"Money per dancer - {prize_for_one_people:.2f}")