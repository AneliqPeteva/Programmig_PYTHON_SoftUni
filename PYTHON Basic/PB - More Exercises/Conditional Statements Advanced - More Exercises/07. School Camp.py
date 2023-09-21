# Read user input
season = input()
group_type = input()
count_student = int(input())
count_night = int(input())
total_sum = 0
# Logic
if group_type == "girls":
    if season == "Winter":
        total_sum = (count_night * 9.60) * count_student
        sport = "Gymnastics"
    elif season == "Spring":
        total_sum = (count_night * 7.20) * count_student
        sport = "Athletics"
    elif season == "Summer":
        total_sum = (count_night * 15.00) * count_student
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        total_sum = (count_night * 9.60) * count_student
        sport = "Judo"
    elif season == "Spring":
        total_sum = (count_night * 7.20) * count_student
        sport = "Tennis"
    elif season == "Summer":
        total_sum = (count_night * 15.00) * count_student
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        total_sum = (count_night * 10.00) * count_student
        sport = "Ski"
    elif season == "Spring":
        total_sum = (count_night * 9.50) * count_student
        sport = "Cycling"
    elif season == "Summer":
        total_sum = (count_night * 20.00) * count_student
        sport = "Swimming"

if count_student < 10:
    total_sum = total_sum
elif 10 >= count_student < 20:
    total_sum *= 0.95
elif count_student < 50:
    total_sum *= 0.85
elif count_student >= 50:
    total_sum *= 0.50


# Print output
print(f"{sport} {total_sum:.2f} lv.")