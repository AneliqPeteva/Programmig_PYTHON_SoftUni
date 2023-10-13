distance_to_the_pokemon = [int(number) for number in input().split()]
total_result = 0
while True:
    if len(distance_to_the_pokemon) <= 0:
        break
    index = int(input())
    result = 0
    if index < 0:
        result += distance_to_the_pokemon[0]
        for current_index in range(0, len(distance_to_the_pokemon)):
            if distance_to_the_pokemon[current_index] <= result:
                distance_to_the_pokemon[current_index] += result
            else:
                distance_to_the_pokemon[current_index] -= result
        distance_to_the_pokemon.pop(0)
        distance_to_the_pokemon.insert(0, distance_to_the_pokemon[-1])

    elif index > len(distance_to_the_pokemon) - 1:
        result += distance_to_the_pokemon[-1]
        for current_index in range(0, len(distance_to_the_pokemon)):
            if distance_to_the_pokemon[current_index] <= result:
                distance_to_the_pokemon[current_index] += result
            else:
                distance_to_the_pokemon[current_index] -= result
        distance_to_the_pokemon.pop()
        distance_to_the_pokemon.insert(distance_to_the_pokemon[-1], distance_to_the_pokemon[0])
    if index in range(0, len(distance_to_the_pokemon)):
        result += distance_to_the_pokemon[index]
        for current_index in range(0, len(distance_to_the_pokemon)):
            if distance_to_the_pokemon[current_index] <= result:
                distance_to_the_pokemon[current_index] += result
            else:
                distance_to_the_pokemon[current_index] -= result
        distance_to_the_pokemon.pop(index)
    total_result += result
print(total_result)