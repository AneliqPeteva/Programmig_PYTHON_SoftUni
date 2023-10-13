population = [int(num) for num in input().split(", ")]
maximum_wealth = int(input())
new_population = []
for current_element in population:
    max_element = max(population)
    index_max_element = population.index(max_element)
    if current_element < maximum_wealth:
        diff = maximum_wealth - current_element
        if max_element - diff >= maximum_wealth:
            population[index_max_element] = max_element - diff
            current_element += diff
            new_population.append(current_element)
    else:
        new_population.append(current_element)

if len(population) == len(new_population):
    print(new_population)
else:
    print("No equal distribution possible")