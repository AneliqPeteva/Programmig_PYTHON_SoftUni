user_input = int(input())
count_ticket = 0
count_other = 0
current_price = int(user_input)
name_buy = input()

while name_buy != "End":
        firts_letter = name_buy[0]
        second_letter = name_buy[1]
        if len(name_buy) > 8:
                price_ticket = ord(firts_letter) + ord(second_letter)
                if price_ticket <= current_price:
                        count_ticket += 1
                        current_price -= price_ticket
                else:
                        break
        else:
                price_other = ord(firts_letter)
                if price_other <= current_price:
                        count_other += 1
                        current_price -= price_other
                else:
                        break
        name_buy = input()

print(f"{count_ticket}")
print(f"{count_other}")

