count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarin_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50

sum_chicken_menu = chicken_menu * count_chicken_menu
sum_fish_menu = fish_menu * count_fish_menu
sum_vegetarian_menu = vegetarian_menu * count_vegetarin_menu
all_sum_menu = sum_chicken_menu + sum_fish_menu + sum_vegetarian_menu
sum_dessert = all_sum_menu * 20/100
total_sum = all_sum_menu + sum_dessert + delivery

print(total_sum)
