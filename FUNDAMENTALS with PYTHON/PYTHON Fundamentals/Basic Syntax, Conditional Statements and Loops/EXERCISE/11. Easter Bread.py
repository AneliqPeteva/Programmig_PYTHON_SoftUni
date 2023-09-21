budget = float(input())
price_flour_1kg = float(input())
counter_bread = 0
counter_color_eggs = 0
total_price_bread = 0
price_for_1_packet_eggs = price_flour_1kg * 0.75
price_for_250ml_milk = (price_flour_1kg + (price_flour_1kg * 0.25)) / 4
price_for_1_bread = price_flour_1kg + price_for_1_packet_eggs + price_for_250ml_milk

while total_price_bread + price_for_1_bread <= budget:
    total_price_bread += price_for_1_bread
    counter_bread += 1
    counter_color_eggs += 3

    if counter_bread % 3 == 0:
        counter_color_eggs -= counter_bread - 2

print(f"You made {counter_bread} loaves of Easter bread! Now you have {counter_color_eggs} eggs and {(budget - total_price_bread):.2f}BGN left.")


