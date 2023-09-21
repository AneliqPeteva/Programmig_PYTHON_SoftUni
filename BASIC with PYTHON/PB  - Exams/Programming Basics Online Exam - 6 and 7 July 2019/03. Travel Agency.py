#User input
name_city = input()
type_packet = input()
vip = input()
count_days = int(input())
total_sum = 0

#logic
if name_city == "Bansko" or name_city == "Borovets":
    if type_packet == "withEquipment":
        total_sum = count_days * 100
        if vip == "yes":
           total_sum = count_days * (100 * 0.90)
    elif type_packet == "noEquipment":
        total_sum = count_days * 80
        if vip == "yes":
           total_sum = count_days * (80 * 0.95)
elif name_city == "Varna" or name_city == "Burgas":
    if type_packet == "withBreakfast":
        total_sum = count_days * 130
        if vip == "yes":
           total_sum = count_days * (130 * 0.88)
    elif type_packet == "noBreakfast":
        total_sum = count_days * 100
        if vip == "yes":
           total_sum = count_days * (100 * 0.93)

if count_days > 7:
    count_days +=1

#print output
if count_days < 1:
    print(f"Days must be positive number!")
elif (name_city == "Bansko" or name_city == "Borovets" or name_city == "Varna" or name_city == "Burgas") and (type_packet == "noEquipment" or type_packet == "withEquipment" or type_packet == "noBreakfast" or type_packet == "withBreakfast") and (vip == "yes" or vip == "no"):
    print(f"The price is {total_sum:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
