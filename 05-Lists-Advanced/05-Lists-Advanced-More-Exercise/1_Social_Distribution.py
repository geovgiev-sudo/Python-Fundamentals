population = list(map(int, input().split(', ')))
minimum_wealth = int(input())

for index, wealth in enumerate(population):
    if wealth < minimum_wealth:
        max_population = population.index(max(population))
        needed_wealth = minimum_wealth - wealth
        population[max_population] -= needed_wealth
        population[index] += needed_wealth

has_needed_wealth = [0 for wealth in population if wealth >= minimum_wealth]

if len(has_needed_wealth) == len(population):
    print(population)
else:
    print("No equal distribution possible")





population = [int(i) for i in input().split(", ")]
min_wealth = int(input())

if sum(population) < min_wealth * len(population):
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            need = min_wealth - population[i]

            while need > 0:
                richest_idx = population.index(max(population))
                available = population[richest_idx] - min_wealth

                if available <= 0:
                    break

                give = min(need, available)
                population[richest_idx] -= give
                population[i] += give
                need -= give

    print(population)








