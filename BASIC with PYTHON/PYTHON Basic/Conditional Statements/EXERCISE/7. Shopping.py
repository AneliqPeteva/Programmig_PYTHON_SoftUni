budget = float(input())
counts_videocards = int(input())
counts_processors = int(input())
counts_ram = int(input())

price_videocard = 250
price_processor = (counts_videocards * price_videocard) * 0.35
price_ram = (counts_videocards * price_videocard) * 0.10

total_sum = counts_videocards * price_videocard + counts_processors * price_processor + counts_ram * price_ram

if counts_videocards > counts_processors:
    total_sum *= 0.85

left_money = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You have {left_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_money:.2f} leva more!")
