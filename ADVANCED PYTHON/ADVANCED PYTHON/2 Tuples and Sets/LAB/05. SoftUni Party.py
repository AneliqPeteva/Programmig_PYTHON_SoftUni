number = int(input())
all_reservations_code = []
vip_quest = []
regular_quest = []
for num in range(number):
    reservation_code = input()
    if reservation_code not in all_reservations_code:
        all_reservations_code.append(reservation_code)

current_reservation_code = input()

while current_reservation_code != "END":
    if current_reservation_code in all_reservations_code:
        all_reservations_code.remove(current_reservation_code)

    current_reservation_code = input()

print(len(all_reservations_code))

sort_all_reservations_code = sorted(all_reservations_code)
for code in sort_all_reservations_code:
    print(code)