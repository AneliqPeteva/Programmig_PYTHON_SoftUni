def accommodate_new_pets(capacity, weight_limit, *args):
    accommodated_pets = {}
    result = ''

    for pet_type, weight in args:
        if not capacity:
            result += 'You did not manage to accommodate all pets!\n'
            break
        if weight > weight_limit:
            continue
        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        capacity -= 1

    else:
        result += f'All pets are accommodated! Available capacity: {capacity}.\n'

    result += 'Accommodated pets:\n'
    for pet, count in sorted(accommodated_pets.items()):
        result += f'{pet}: {count}\n'

    return result



# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))
#
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
#
# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))


