number_of_snowballs = int(input())
max_point_for_snowballs = 0
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0
for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value_snowball = (snowball_weight / snowball_time) ** snowball_quality
    if value_snowball > max_point_for_snowballs:
        max_point_for_snowballs = value_snowball
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_point_for_snowballs)} ({max_snowball_quality})")