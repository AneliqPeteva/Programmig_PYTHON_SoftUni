def accommodate_new_pets(available_capacity_hotel, maximum_weight, *args):
    available_capacity_hotel = int(available_capacity_hotel)
    maximum_weight = float(maximum_weight)

    hotel = {}
    result = ""

    for pet_type, pet_weight in args:
        if available_capacity_hotel == 0:
            break

        if pet_weight > maximum_weight:
            continue

        if pet_weight <= maximum_weight:
            if pet_type not in hotel:
                hotel[pet_type] = 0
            hotel[pet_type] += 1
            available_capacity_hotel -= 1




    if available_capacity_hotel > 0:
        result += f"All pets are accommodated! Available capacity: {available_capacity_hotel}."
    else:
        result += "You did not manage to accommodate all pets!"



    hotel = sorted(hotel.items(), key=lambda x: x[0])
    result += f"\nAccommodated pets:"
    for type, count in hotel:
        result += f"\n{type}: {count}"

    return result



print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


