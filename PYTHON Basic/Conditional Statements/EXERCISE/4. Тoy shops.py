price_excursion = float(input())
count_puzzle = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

count_toys = count_puzzle + count_dolls + count_bears + count_minions + count_trucks
sum_toys = count_puzzle * price_puzzle + count_dolls * price_doll + count_bears * price_bear + count_minions * price_minion + count_trucks * price_truck

if count_toys >= 50:
    sum_toys = sum_toys - sum_toys * 0.25
else:
    sum_toys == sum_toys

rent = sum_toys * 0.10
earnings = sum_toys - rent

if earnings >= price_excursion:
    print(f"Yes! {earnings - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money!{price_excursion - earnings: .2f} lv needed.")