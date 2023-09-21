count_customers = int(input())
basket = 1.50
wreath = 3.80
chocolate_bunny = 7.00
total_price = 0


for i in range(count_customers):
    purchase = input()
    count = 0
    all_price = 0
    while purchase != "Finish":
        count += 1
        if purchase == "basket":
            all_price += basket
        elif purchase == "wreath":
            all_price += wreath
        elif purchase == "chocolate bunny":
            all_price += chocolate_bunny

        purchase = input()

    if count % 2 == 0:
        all_price -= all_price * 0.20
    total_price += all_price
    print(f"You purchased {count} items for {all_price:.2f} leva.")

print(f"Average bill per client is: {total_price / count_customers:.2f} leva.")