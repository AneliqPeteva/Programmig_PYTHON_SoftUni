#lost_fights_count = int(input())
#helmet_price = float(input())
#sword_price = float(input())
#shield_price = float(input())
#armor_price = float(input())
#helmet_count = 0
#sword_count = 0
#shield_count = 0
#armor_count = 0
#for current_fight in range(1, lost_fights_count + 1):
#    if current_fight % 2 == 0:
#        helmet_count += 1
#    if current_fight % 3 == 0:
#        sword_count += 1
#        if current_fight % 2 == 0:
#            shield_count += 1
#            if shield_count % 2 == 0:
#                armor_count +=1
#
#expenses = helmet_count * helmet_price + sword_count * sword_price + shield_count * shield_price + armor_count * armor_price
#print(f"Gladiator expenses: {expenses:.2f} aureus")


number_lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = number_lost_fights_count // 2
total_sword_broken = number_lost_fights_count // 3
total_shield_broken = number_lost_fights_count // (2 * 3)
total_armor_broken = total_shield_broken // 2

expenses = (total_helmet_broken * helmet_price \
            + total_sword_broken * sword_price \
            + total_shield_broken * shield_price \
            + total_armor_broken * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")

